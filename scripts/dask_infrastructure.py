import sys
import json
from typing import List
from common import replace_special_characters, append_content_to_end_of_file

def edit_dbx_teams_output_file(params):
    file_path: str = "terraform/modules/dbx_teams/outputs.tf"
    project_name: str = params.get("project_name")
    
    content = f'''
    output "{project_name.lower()}_catalog_name" {{
      value = "module.{project_name.lower()}.catalog_name"  
    }}
    '''
    append_content_to_end_of_file(file_path, content)
    

def edit_dbx_teams_file(filepath, params):
    project_name: str = params.get("project_name")

    ad_group_name: str = params["ad_groups"][0]
    area_name: str = params["area_name"]
    project_id_map: dict = params["gcp_project_ids"]

    # Define the new team data
    new_team_data = generate_module_definition(ad_group_name, area_name, project_name, project_id_map)

    append_content_to_end_of_file(filepath, new_team_data)

def generate_module_definition(ad_group_name: str, area_name: str, project_name: str, project_id_map: dict) -> str: 
    area_special_chars_replaced = replace_special_characters(area_name)
    module = f'''
    module "{project_name.lower()}" {{
      source = "../dbx_team_resources"

      ad_group_name = "AAD - TF - TEAM - {ad_group_name}"
      team_name     = "{project_name.lower()}"
      area_name     = "{area_special_chars_replaced.lower()}"
      deploy_sa_map = {{
        sandbox = "{project_name.lower()}-deploy@{project_id_map['sandbox']}.iam.gserviceaccount.com",
        dev     = "{project_name.lower()}-deploy@{project_id_map['dev']}.iam.gserviceaccount.com",
        prod    = "{project_name.lower()}-deploy@{project_id_map['prod']}.iam.gserviceaccount.com"
      }}
      projects = {{
        sandbox = "{project_id_map['sandbox']}",
        dev     = "{project_id_map['dev']}",
        prod    = "{project_id_map['prod']}",
      }}
        
      marketplace_sa_map = local.marketplace_sa_map
        
      providers = {{
        databricks.accounts   = databricks.accounts
        databricks.workspace  = databricks.workspace
        google.global_storage = google.global_storage
      }}

      metastore_id              = var.metastore_id
      workspace_id              = var.workspace_id
      workspace_env             = var.workspace_env
      env                       = var.env
      all_users_group_id        = var.all_users_group_id
      product_teams_group_id    = var.product_teams_group_id
      compute_sa_teams_group_id = var.compute_sa_teams_group_id
    }}
    '''

    return module


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python script.py <file_path> <json_object>")
        sys.exit(1)

    file_path = sys.argv[1]
    json_str = sys.argv[2]
    params = json.loads(json_str)

    edit_dbx_teams_file(file_path, params)
    edit_dbx_teams_output_file(params)
