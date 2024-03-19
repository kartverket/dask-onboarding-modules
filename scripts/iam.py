import json
import sys
from typing import List


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

        lines = file.readlines()
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
