import json
import sys
from typing import List


def find_line_ref_local_teams(lines: List[str]) -> int:
    for (row, idx) in zip(lines, range(len(lines))):
        if row.startswith('  teams_v2 = {'):
            return idx
        

def edit_file(file_path, params):
    with open(file_path) as file:
        project_name: str = params.get("project_name")
        ad_group: str = params.get("ad_groups")[0]

        print("Project Name:", project_name)
        print("AD Groups:", ad_group)

        lines = file.readlines()
        file.close()

        last_teams_ref_idx = find_line_ref_local_teams(lines)
        ad_group_formatted = json.dumps(ad_group).replace(' ', '').replace('"', '').lower()
        lines.insert(last_teams_ref_idx + 3, f'"{project_name}"= ["aad-tf-team-{ad_group_formatted}@kartverket.no", "aad-tf-team-dataplattform@kartverket.no"]\n')

        with open(file_path, 'w') as file:
            file.writelines(lines)
            file.close()


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python script.py <file_path> <json_object>")
        sys.exit(1)

    file_path = sys.argv[1]
    json_str = sys.argv[2]
    params = json.loads(json_str)

    edit_file(file_path, params)
