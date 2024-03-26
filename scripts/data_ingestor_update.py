import json
import sys

envs = ["sandbox", "dev", "test", "prod"]

def should_keep_line(line: str) -> bool:
    lines_to_keep = ["databricks_workspace_url", "environment"]
    for line_to_keep in lines_to_keep:
        if line_to_keep in line:
            return True
    
    return False

def update_tfvar_file(monorepo_folder_path: str, env: str, team_name: str, project_id: str, project_number: str):
    tfvars_path = f'{monorepo_folder_path}/terraform/variables/{env}.tfvars'
    
    with open(tfvars_path) as file:
        lines = list(filter(should_keep_line, file.readlines()))
        file.close()

        lines.insert(0, f'repo_name = "{team_name.lower()}-data-ingestor"\n')
        lines.insert(0, f'landing_zone_bucket = "landing-zone-{project_id}"\n')
        lines.insert(0, f'compute_service_account = "databricks-compute@${project_id}.iam.gserviceaccount.com"\n')
        lines.insert(0, f'deploy_service_account = "{team_name.lower()}-deploy@{project_id}.iam.gserviceaccount.com"\n')
        lines.insert(0, f'project_number = "{project_number}"\n')
        lines.insert(0, f'project_id = "{project_id}"\n')

        with open(tfvars_path, 'w') as file:
            file.writelines(lines)
            file.close()


def update_state_bucket(monorepo_folder_path: str, env: str, val_for_env: str) -> None:
    with open(f'{monorepo_folder_path}/terraform/backend/{env}.gcs.tfbackend', 'w') as file:
        file.write(f'bucket = "{val_for_env}"\n')
        file.close()


def copy_and_paste_github_deploy_workflow(file_path: str, env: str):
    workflows_path = f'{file_path}/.github/workflows'
    
    with open(f'{workflows_path}/deploy-sandbox.yml') as file:
        lines = file.readlines()
        file.close()

        with open(f'{workflows_path}/deploy-{env}.yml', 'w') as file:
            file.writelines(lines)
            file.close()

def update_databricks_config(file_path: str, area_name: str, team_name: str):
    config_path = f'{file_path}/src/databricks/config.py'
    
    with open(config_path, 'r') as file:
        lines = [line.replace("plattform_dataprodukter", f"{area_name.lower()}_{team_name.lower()}") for line in file.readlines()]
        file.close()

        with open(config_path, 'w') as file:
            file.writelines(lines)
            file.close()


def clear_codeowners(file_path: str, team_name: str):
    codeowners_path = f'{file_path}/CODEOWNERS'
    
    with open(codeowners_path, 'r') as file:
        file_content = file.read()
        file_content = file_content.replace("Team DASK (Dataplattform Statens Kartverk)", f"Team {team_name}")
        file_content = file_content.replace("@jonasmw94 @JoachimHaa @augustdahl @Ed0rF", "<<enter team members (@username) here>>")
        file_content = file_content.replace("@augustdahl", "<<enter security champion (@username) here>>")
        file.close()

        with open(codeowners_path, 'w') as file:
            file.write(file_content)
            file.close()


def configure_github_deploy_workflow(file_path: str, env: str, team_name: str, project_id: str, project_number: str):
    workflows_path = f'{file_path}/.github/workflows'

    sa_to_replace = "dataplattform-deploy@dataprodukter-sandbox-4413.iam.gserviceaccount.com"
    project_number_to_replace = "364051313161"
    project_id_to_replace = "dataprodukter-sandbox-4413.iam.gserviceaccount.com"
    repo_to_replace = "dask-monorepo-reference-setup"
    team_name_to_replace = "dataprodukter"
    env_to_replace = "sandbox"

    replacement_tuples = [
        (project_number_to_replace, project_number),
        (sa_to_replace, f'{team_name.lower()}-deploy@{project_id}.iam.gserviceaccount.com'),
        (project_id_to_replace, project_id),
        (repo_to_replace, f'{team_name.lower()}-data-ingestor'),
        (team_name_to_replace, team_name.lower()),
        (env_to_replace, env)
    ]
    
    with open(f'{workflows_path}/deploy-{env}.yml') as file:
        lines = file.readlines()
        file.close()
        
        for replacement in replacement_tuples:
            lines = [line.replace(replacement[0], replacement[1]) for line in lines]
    
        with open(f'{workflows_path}/deploy-{env}.yml', 'w') as file:
            file.writelines(lines)
            file.close()


def edit_file(file_path, json_obj):
    team_name: str = json_obj.get("team_name")
    area_name: str = json_obj.get("area_name")

    clear_codeowners(file_path, team_name)
    update_databricks_config(file_path, area_name, team_name)

    # Setup github actions files to be used later
    for env in envs:
        copy_and_paste_github_deploy_workflow(file_path, env)

    for env in envs:
        state_bucket_for_env = json_obj.get("gcp_state_buckets")[env]
        update_state_bucket(file_path, env, state_bucket_for_env)

        project_id_for_env = json_obj.get("gcp_project_ids")[env]
        auth_project_number_for_env = json_obj.get("gcp_auth_numbers")[env]
        update_tfvar_file(file_path, env, team_name, project_id_for_env, auth_project_number_for_env)
        configure_github_deploy_workflow(file_path, env, team_name, project_id_for_env, auth_project_number_for_env)


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python script.py <file_path> <json_object>")
        sys.exit(1)

    file_path = sys.argv[1]
    json_str = sys.argv[2]
    json_obj = json.loads(json_str)

    edit_file(file_path, json_obj)

# python data_ingestor_update.py './dask-monorepo-reference-setup' '{ "team_name": "TestTeam", "area_name": "TestAvd", "project_id_sandbox": "project-sandbox", "project_id_dev": "project-dev", "project_id_test": "project-test", "project_id_prod": "project-prod", "auth_project_number_sandbox": "auth_project_number-sandbox", "auth_project_number_dev": "auth_project_number-dev", "auth_project_number_test": "auth_project_number-test", "auth_project_number_prod": "auth_project_number-prod", "state_bucket_sandbox": "state_bucket-sandbox", "state_bucket_dev": "state_bucket-dev", "state_bucket_test": "state_bucket-test", "state_bucket_prod": "state_bucket-prod" }'
