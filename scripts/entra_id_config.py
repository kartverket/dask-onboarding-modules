import json
import sys
from common import append_content_to_end_of_file


def create_team_entraid_modul(team_name: str, product_area: str, team_lead: str) -> str:
    entraid_modul = f'''
    module "{"_".join(team_name.lower().split())}" {{
        source    = "./modules/team"
        team_name = "{team_name}"
        parent_group_object_id = module.{product_area.lower()}.business_unit_object_id
        team_lead              = "{team_lead}"
        azuread_variables      = module.azuread_variables
        enable_databricks      = true
    }}
    '''

    return entraid_modul


def edit_file(file_path: str, params: str):
    team_name: str = params.get("team_name")
    product_area: str = params.get("product_area")
    team_lead = params["team_lead"]

    team_entraid_config = create_team_entraid_modul(team_name, product_area, team_lead)
    append_content_to_end_of_file(file_path + f'/{product_area.lower()}.tf', team_entraid_config)


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python script.py <file_path> <json_object>")
        sys.exit(1)

    file_path = sys.argv[1]
    json_str = sys.argv[2]
    params = json.loads(json_str)

    edit_file(file_path, params)
