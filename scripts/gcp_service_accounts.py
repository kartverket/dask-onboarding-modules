import json
import sys
from typing import List


def generate_module_definition(team_name: str) -> str: 
    module = f'''
    module "{team_name.lower()}" {{
        source    = "./project_team"
        team_name = "{team_name}"
        repositories = [
            "kartverket/{team_name.lower()}-data-ingestor",
        ]
        extra_team_sa_roles = [
            "roles/resourcemanager.projectIamAdmin",
            "roles/iam.serviceAccountTokenCreator",
            "roles/iam.serviceAccountUser",
            "roles/secretmanager.admin",
            "roles/storage.admin",
            "roles/serviceusage.serviceUsageAdmin",
            "roles/cloudfunctions.admin",
            "roles/cloudscheduler.admin"
        ]
        env                   = var.env
        project_id            = var.{team_name.lower()}_project_id
        kubernetes_project_id = var.kubernetes_project_id
        can_manage_sa         = true
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

def edit_file(file_path, json_obj):
    team_name: str = json_obj.get("team_name")
    project_ids = json_obj["gcp_project_ids"]
    project_id_sandbox = project_ids["sandbox"]
    project_id_dev = project_ids["dev"]
    project_id_test = project_ids["test"]
    project_id_prod = project_ids["prod"]

    # Handle modules.tf
    module_definition = generate_module_definition(team_name)
    append_content_to_end_of_file(file_path + "/modules.tf", module_definition)

    # Handle variables.tf
    variable_def = f'variable "{team_name.lower()}_project_id" {{}}\n'
    append_content_to_end_of_file(file_path + "/variables.tf", variable_def)

    # Handle *.tfvars files
    get_project_var_entry = lambda project: f'\n{team_name.lower()}_project_id = "{project}"'
    
    sandbox_var_entry = get_project_var_entry(project_id_sandbox)
    append_content_to_end_of_file(file_path + "/sandbox.tfvars", sandbox_var_entry)

    dev_var_entry = get_project_var_entry(project_id_dev)
    append_content_to_end_of_file(file_path + "/dev.tfvars", dev_var_entry)

    test_var_entry = get_project_var_entry(project_id_test)
    append_content_to_end_of_file(file_path + "/test.tfvars", test_var_entry)

    prod_var_entry = get_project_var_entry(project_id_prod)
    append_content_to_end_of_file(file_path + "/prod.tfvars", prod_var_entry)


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python script.py <file_path> <json_object>")
        sys.exit(1)

    file_path = sys.argv[1]
    json_str = sys.argv[2]
    json_obj = json.loads(json_str)

    edit_file(file_path, json_obj)

# python gcp_service_accounts.py './path/to/gcp_service_accounts' '{ "team_name": "TestTeam", "project_id_sandbox": "project-sandbox", "project_id_dev": "project-dev", "project_id_test": "project-test", "project_id_prod": "project-prod"  }'