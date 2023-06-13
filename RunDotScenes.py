from cognata_api.web_api.cognata_demo import CognataRequests as cog_api
from Processing.RunningScenario import Run
from Processing.DownloadingScenarios import Download
from Processing.WorkBook import CreateWorkbook
from Processing.WorkBookUniqueColumns import AddUniqueColumns as AUC

from Utils.DataFolder import DataFolder
from Utils import GenericFunctions, Paths, Bridge
import json, sys, os


# Getting user API
def connect_to_backend(user_details):
    # variables definition
    username = user_details['user_name']
    password = user_details['password']
    company_id = user_details['company_id']
    backendIP = "https://{}-api.cognata-studio.com/v1".format(company_id)

    # Create api connection to studio cloud instance
    # connects through API url
    api_connection = cog_api(backendIP, username, password)
    if not api_connection.is_logged_in:
        raise ValueError("illegal details")
    return api_connection


def find_scenario(api_connection, search_string):
    return api_connection._perform_get_request("{api_url}/scenarios".format(api_url=api_connection.client_api_url),
                                               query_params={"searchString": search_string})


def get_all_scenarios(api_connection):
    return api_connection._perform_get_request("{api_url}/scenarios".format(api_url=api_connection.client_api_url))


def start_simulation(api_connection, scenario_formula, client = "stats_algo_v1:1.19.0"):
    return api_connection.generate_simulation(scenario_formula, client, annotate=False)


def get_scenario_formula(api_connection, scenario_id):
    return api_connection._perform_get_request(
        "{api_url}/scenarios/{scene_id}".format(api_url=api_connection.client_api_url, scene_id=scenario_id))


def get_scene_id_from_simulations(api_connection, scene_id):
    return api_connection._perform_get_request(
        "{api_url}/simulations/{scene_id}".format(api_url=api_connection.client_api_url, scene_id=scene_id))

'''
get_weather_conditions()

get_time_of_day()

get_ai_cars_list()

get_ego_cars_list()
'''
# opening json files and getting user details variables
with open(Paths.Folder('user_details.json'), 'r') as f:
    user_details = json.load(f)

with open(Paths.Folder('variables.json'), 'r') as f:
    data = json.load(f)

print(Paths.Folder('dot_scenes'))
# defining api variable
api = connect_to_backend(user_details)

# creating df object
df_name = data['df_name']
df = DataFolder(df_name)

# running all simulations
n_runs = int(data['n_runs'])
scene_name = data['scene_name'] + ".json"
ego_preset = data['ego_preset']
client = data['client'] + ":1.19.0"
# Run(api, df, n_runs, scene_script_name, scene_id, ego_preset, client)
with open(Paths.Folder(scene_name), 'r') as f:
    scene_formula = json.load(f)

# print(scene_formula)
for _ in range(n_runs):
    start_simulation(api, scene_formula)

# # downloading scenarios data by using user connection to cognata studio
# Download(api, df)

# # creating Excel file with simulations data
# groups = int(data['groups'])
# CreateWorkbook(df, groups)

# # adding unique columns
# unique_columns = data['unique_columns']
# print("df.folder_path", df.folder_path)
# print("df.groups", df.groups)
# print("unique_columns", unique_columns)

# AUC(df.folder_path, df.groups, unique_columns)

# # printing data folder details and deleting temp file
# df.PrintingDFDetails()
# df.deleting_temp_file()






# api = connect_to_backend()
# all_scenarios = get_all_scenarios(api)
# print("amount of scenarios in cognata server is = " + str(len(all_scenarios)))
# dot_scenarios_list = find_scenario(api, "dot")
# print("len of dot scenarios list = " + str(len(dot_scenarios_list)))
# first_dot_formula = get_scenario_formula(api, dot_scenarios_list[0]['_id'])
# print(first_dot_formula)
# for key in first_dot_formula.keys():
#     print(key + ":")
#     print(first_dot_formula[key])
# # print("first dot formula: " + str(first_dot_formula))
# start_first_dot = start_simulation(api, first_dot_formula)
# print("new simulation id is: " + str(start_first_dot))
# for scene in dot_scenarios_list:
#     formula = get_scenario_formula(api, scene['id'])
#     json_string = json.dumps(formula)
#     f = open("{scene_name}.json".format(scene_name=formula['name']), "w")
#     f.write(json_string)
#     f.close()