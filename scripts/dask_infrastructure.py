import sys
import os


def edit_file(filepath):
    with open(filepath, 'r') as file:
        lines = file.readlines()

    # Define the new team data
    new_team_data = """
      "new_team" : {
        "members" : [
          "member1@example.com",
          "member2@example.com"
        ],
        "external_users" : [],
        "area_name" : "new_area",
        "deploy_service_account" : {
          "sandbox" : "new-team-deploy@sandbox.iam.gserviceaccount.com",
          "dev" : "new-team-deploy@dev.iam.gserviceaccount.com"
        },
        "project_id" : {
          "sandbox" : "new-team-sandbox",
          "dev" : "new-team-dev"
        }
      },
    """

    # Find the end of the 'locals' block and insert the new team data
    insert_index = next((i for i, line in enumerate(
        reversed(lines)) if line.strip() == "},"), None)
    if insert_index is not None:
        lines.insert(len(lines) - insert_index, new_team_data)

    with open(filepath, 'w') as file:
        file.writelines(lines)


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python edit_file.py <path-to-file> <script-params>")
        sys.exit(1)

    file_path = sys.argv[1]
    absolute_path = os.path.abspath(file_path)
    print(f"Attempting to access: {absolute_path}")
    edit_file(file_path)
