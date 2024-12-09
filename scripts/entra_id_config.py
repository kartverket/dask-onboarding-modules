import sys
import yaml

def read_yaml_file(file):
    with open(file, 'r') as f:
        yaml_data=yaml.safe_load(f)
    return yaml_data

def modify_yaml_with_params(data: dict, params: dict):
    
    area_name = params.get("area_name")
    team_name = params.get("team_name")
    team_lead = params.get("team_lead")


    newteamdata = {
        area_name: {
            "name": area_name.title(),
            "teams": {
                team_name: {
                    "enable_databricks": True,
                    "name": team_name.title(),
                    "team_lead": team_lead,
                }
            }
        }
    }

    
    for key, value in newteamdata.items():
        if key in data:
            print(key)
            data[key]["teams"].update(value["teams"])
        else:
            data.update(value)

    return data

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python script.py <file_path> <json_object>")
        sys.exit(1)

    file_path = sys.argv[1]
    params = {"area_name": "land", "project_name": "team_test", "shouldCreateNewTeam": True,"team_lead": "test.testesen@kartverket.no", "team_name": "TeamTest"}
    
    data = modify_yaml_with_params(read_yaml_file(sys.argv[1]), params)
    print(yaml.dump(data))