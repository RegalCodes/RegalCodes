import requests
from datetime import datetime
import os
# print(os.environ) to see all of env variables
from requests.auth import HTTPBasicAuth
#sheety.co for google sheets api

APP_ID = "312d12ae"
API_KEY = "9c078a50983781f83a574406cfcb598a"

#to create ENV key, type in terminal, export "variable name"="Data" you want to hide

Exercise_Endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
Sheety_Endpoint = "https://api.sheety.co/b97f5ca7ddf85aeb11e2a610c0e4f516/workoutTracking/workouts"


exercise_text = input("Tell me which exercise you did: ")
gender = "male"
weight_kg = 96.5
height_cm = 172.72
age = 25

headers = {
 "x-app-id": APP_ID,
 "x-app-key": API_KEY,
}

post_params = {
 "query": exercise_text,
 "gender": gender,
 "weight_kg": weight_kg,
 "height_cm": height_cm,
 "age": age,
}

response = requests.post(url=Exercise_Endpoint, json=post_params,headers=headers)
result = response.json()
# print(result)

#step 4

today_date = datetime.now().strftime("%m/%d/%Y")
now_time = datetime.now().strftime("%X")
#https://www.w3schools.com/python/python_datetime.asp

for exercise in result["exercises"]:
    sheet_inputs = {
      "workout": {
        "date": today_date,
        "time": now_time,
        "exercise": exercise["name"].title(),
        "duration": exercise["duration_min"],
        "calories": exercise["nf_calories"],
      }
    }

sheet_response = requests.post(url=Sheety_Endpoint, json=sheet_inputs, auth=("regal","regalworkout15"))


print(sheet_response.text)

#step 5
	#Basic Authentication
# sheet_response = requests.post(
#   Sheety_Endpoint,
#   json=sheet_inputs,
#   auth=(
#       YOUR USERNAME,
#       YOUR PASSWORD,
#   )
# )
