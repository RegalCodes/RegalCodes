import requests
from datetime import datetime

#get - get info  # post - post data # put -> Update # Delete -> Delete
USERNAME = "regal"
TOKEN = "232sd462fv2r3"

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",

}

#step 1 to creating user
# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": "graph1",
    "name": "Running Miles",
    "unit": "Mi",
    "type": "float",
    "color": "momiji",
}

headers = {
    "X-USER-TOKEN": TOKEN
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

#https://pixe.la/v1/users/regal/graphs/graph1.html

post_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/graph1"

today = datetime.now()
# today = datetime(year=2021, month=12, day=4)
print(today.strftime("%Y%m%d"))

post_body = {
    "date": today.strftime("%Y%m%d"),
    "quantity": input("How many miles did you run today?"),
}

response = requests.post(url=post_endpoint,json=post_body, headers=headers)
print(response.text)


update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/graph1/{today.strftime('%Y%m%d')}"

new_pixel_data = {
    "quantity": "4.5"
}

# response = requests.put(url=update_endpoint, json=new_pixel_data, headers=headers)
# print(response.text)
#requests.put to update an existing data.

delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/graph1/{today.strftime('%Y%m%d')}"
# response = requests.delete(url=delete_endpoint, headers=headers)
# print(response.text)
#requests.delete to delete an existing data.