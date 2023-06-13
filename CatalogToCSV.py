import sys 
import cognata_api.web_api.cognata_demo as api
sys.path.append("..")
from CognataUtils import SpawnUtils as SpawnUtils




## Connect to server
company_id = "2a4ab8d2"
username = "gavriel"
password = "Aa123456"
# client_queue = ''
backendIP = f"https://{company_id}.cognata-studio.com/v1"

cognata_api = api.CognataRequests(backendIP, username, password)
if not cognata_api.is_logged_in:
    raise ValueError("Please fill in the variables in the designated cell")

assets_by_type = SpawnUtils.get_assets_by_spawn_type(cognata_api)
static_assets = assets_by_type['movingObjects']
print('static_assets', static_assets)
file_object = open("assets_list.csv", "w")
file_object.write("Name,BrandID\n")
print('file_object:', file_object)
print('file_object type:', type(file_object))

for asset_temp in static_assets:
    file_object.write(asset_temp['label']+","+asset_temp['value']+"\n")
file_object.close()