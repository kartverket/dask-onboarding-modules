import sys
import os
import json

def edit_file(filepath, json_obj):
    team_name: str = json_obj.get("team_name")
    ad_group_name: str = json_obj.get("ad_group_name")
    area_name: str = json_obj.get("area_name")
    project_id = {}
    project_id["sandbox"] = json_obj.get("project_id_sandbox")
    project_id["dev"] = json_obj.get("project_id_dev")
    project_id["test"] = json_obj.get("project_id_test")
    project_id["prod"] = json_obj.get("project_id_prod")

    # Define the new team data
    new_team_data = generate_module_definition(ad_group_name, team_name, area_name, project_id)

    append_content_to_end_of_file(filepath, new_team_data)

def generate_module_definition(ad_group_name: str, team_name: str, area_name: str, project_id_map: dict) -> str: 
    module = f'''
    module "{team_name.lower()}" {{
      source = "../dbx_team_resources"

      ad_group_name = "{ad_group_name}"
      team_name     = "{team_name.lower()}"
      area_name     = "{area_name.lower()}"
      deploy_sa_map = {{
        sandbox = "{team_name.lower()}-deploy@{project_id_map['sandbox']}.iam.gserviceaccount.com",
        dev     = "{team_name.lower()}-deploy@{project_id_map['dev']}.iam.gserviceaccount.com",
        test    = "{team_name.lower()}-deploy@{project_id_map['test']}.iam.gserviceaccount.com",
        prod    = "{team_name.lower()}-deploy@{project_id_map['prod']}.iam.gserviceaccount.com"
      }}
      projects = {{
        sandbox = "{project_id_map['sandbox']}",
        dev     = "{project_id_map['dev']}",
        test    = "{project_id_map['test']}",
        prod    = "{project_id_map['prod']}",
      }}

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

def append_content_to_end_of_file(file_path: str, content: str) -> None:
    with open(file_path) as file:
        lines = file.readlines()
        file.close()
        lines.insert(len(lines), content)

        with open(file_path, 'w') as file:
            file.writelines(lines)
            file.close()



if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python edit_file.py <path-to-file> <script-params>")
        sys.exit(1)

    file_path = sys.argv[1]
    json_str = sys.argv[2]
    json_obj = json.loads(json_str)

    edit_file(file_path, json_obj)
