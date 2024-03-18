import json
import sys
from typing import List

module_template = lambda x : '''
module "__teamname__" {
    source                = "./product-team"
    team                  = "__teamname_cap__"
    members               = ["__teamname_cap__"]
    env                   = var.env
    parent_folder         = google_folder.teams.name
    monitoring_project_id = var.monitoring_project_id
}
'''.replace("__teamname__", x.lower()).replace("__teamname_cap__", x)


def find_last_team_module_line_idx(lines: List[str]) -> int:
    last_idx = 0
    for (row, idx) in zip(lines, range(len(lines))):
        if row.startswith('module "') and not row.startswith('module "team"'):
            last_idx = idx
    
    return last_idx


def find_line_ref_local_teams(lines: List[str]) -> int:
    for (row, idx) in zip(lines, range(len(lines))):
        if row.startswith('  teams = {'):
            return idx
        

def edit_file(file_path, json_obj):
    with open(file_path) as file:
        team_name: str = json_obj.get("team_name")
        ad_groups: List[str] = json_obj.get("ad_groups")

        print("Team Name:", team_name)
        print("AD Groups:", ad_groups)

        new_team_data = module_template(team_name)

        lines = file.readlines()
        last_module_idx = find_last_team_module_line_idx(lines)
        lines.insert(last_module_idx - 1, new_team_data)
        file.close()

        last_teams_ref_idx = find_line_ref_local_teams(lines)
        lines.insert(last_teams_ref_idx + 3, f'"{team_name}"= {json.dumps(ad_groups)},\n')

        with open(file_path, 'w') as file:
            file.writelines(lines)
            file.close()


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python script.py <file_path> <json_object>")
        sys.exit(1)

    file_path = sys.argv[1]
    json_str = sys.argv[2]
    json_obj = json.loads(json_str)

    edit_file(file_path, json_obj)
