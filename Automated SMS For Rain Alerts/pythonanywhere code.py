import requests
import os
from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient

#https://help.pythonanywhere.com/pages/TwilioBehindTheProxy/

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/onecall"
api_key = "78279ddf53822d983eaefca6aaf2742e"
account_sid = "AC1ca5ce1a5428553e523153287b7c802b"
auth_token = "de04e2548e07e41bc7e4eae1a59a5a74"

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
    proxy_client = TwilioHttpClient()
    proxy_client.session.proxies = {'https': os.environ['https_proxy']}
    client = Client(account_sid, auth_token, http_client=proxy_client)
    message = client.messages \
        .create(
        body="It's going to rain today, Remember to bring an  ☂️",
        from_='+12057971072',
        to='+12096392652'
    )
    print(message.status)


    # print("Bring an umbrella")

# print(weather_data["hourly"][0]["weather"][0]["id"])

#Json Parsing