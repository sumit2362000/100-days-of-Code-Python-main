
import requests
from datetime import date, datetime

'''
HTTP requests
get() - request data from external system and receive data back
post() - send data to external system, not interested in receiving data
put() - update data in external service, like updating google docs
delete() - delete piece of data in external service
'''

'''
post habit tracking data to pixela to be tracked
https://pixe.la/
https://docs.pixe.la/
https://docs.python-requests.org/en/latest/api/
'''

# https://pixe.la/v1/users/afe4ther/graphs/graph1.html

USERNAME = "afe4ther"
TOKEN = "afe4ther_pixe.la"
GRAPH_ID = "graph1"

'''Create a user on pixe.la'''
pixela_endpoint = "https://pixe.la/v1/users"
pixela_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}
# response = requests.post(url=pixela_endpoint,json=pixela_params)

'''Create Graph'''
# https://pixe.la/v1/users/afe4ther/graphs/graph1.html
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
graph_config = {
    "id":GRAPH_ID,
    "name":"Cycling Graph",
    "unit": "Km",
    "type": "float",
    "color": "ajisai",
}
headers = {
    "X-USER-TOKEN": TOKEN,
}
# graph_request = requests.post(url=graph_endpoint,json=graph_config,headers=headers)

'''Post a Pixel'''
yesterday = datetime(year=2021,month=6,day=25).strftime("%Y%m%d")
# today = datetime.now()
pixel_params = {
    "date": yesterday,
    "quantity": "11.11",
}
update_graph_endpoint = f"{graph_endpoint}/{GRAPH_ID}"
# update_graph_request = requests.post(url=update_graph_endpoint,json=pixel_params,headers=headers)

'''Update yesterday's pixel'''
new_pixel_params = {
    "quantity": "10.10",   
}
update_pixel_endpoint = f"{update_graph_endpoint}/{yesterday}"
# pixel_update = requests.put(url=update_pixel_endpoint,json=new_pixel_params,headers=headers)
# print(pixel_update)

'''Delete pixel'''
# https://docs.pixe.la/entry/delete-pixel