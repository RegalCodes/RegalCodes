import requests
from twilio.rest import Client

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/onecall"
api_key = "78279ddf53822d983eaefca6aaf2742e"
account_sid = "AC1ca5ce1a5428553e523153287b7c802b"
auth_token = "de04e2548e07e41bc7e4eae1a59a5a74"

#https://openweathermap.org/api/one-call-api#
#https://home.openweathermap.org/api_keys#
#latlong.net#
#twilio.com , pythonanywhere.com
#jsonview.stack.hu

weather_params = { "lat": 14.034820,
                   "lon": -83.383698,
                   "appid": api_key,
                   "exclude": "current,minutely,daily"

}

response = requests.get(OWM_Endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()
# print(response.status_code)
weather_slice = weather_data["hourly"][:12]
print(weather_slice)

will_rain = False

for hour_data in weather_slice:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True


if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="It's going to rain today, Remember to bring an  ☂️",
        from_='+12057971072',
        to='+12096392664'
    )
    print(message.status)


    # print("Bring an umbrella")

# print(weather_data["hourly"][0]["weather"][0]["id"])

#Json Parsing

#environment code  , Go to Terminal then type env , then type export own_api_key="OWM_API_KEY" , without the quotes and it'll show up in the env. type env again
#to call the variable back from environment,  api_key = os.environ.get("OWM_API_KEY")
