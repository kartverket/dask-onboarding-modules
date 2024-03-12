import json
import sys


def edit_file(file_path, json_obj):
    with open(file_path) as file:
        data = json.load(file)

    team_name = json_obj.get("team_name")
    ad_groups = json_obj.get("ad_groups")

    print("Team Name:", team_name)
    print("AD Groups:", ad_groups)


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python script.py <file_path> <json_object>")
        sys.exit(1)

    file_path = sys.argv[1]
    json_str = sys.argv[2]
    json_obj = json.loads(json_str)

    edit_file(file_path, json_obj)
