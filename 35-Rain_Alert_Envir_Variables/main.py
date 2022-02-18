
import requests
from requests import api
#Twilio
from twilio.rest import Client
# https://www.twilio.com/console
# Twilio Trial Phone Number: (812) 594-4188
TWILIO_ACCOUNT_SID = 'AC393ae015001a9ac56f251a24bfa4b437'
TWILIO_AUTH_TOKEN = '272340dbc24be6dd073da81b7aed34ca'
account_sid = TWILIO_ACCOUNT_SID
auth_token = TWILIO_AUTH_TOKEN

'''
Website: https://openweathermap.org/api/one-call-api
https://api.openweathermap.org/data/2.5/onecall?lat={lat}&lon={lon}&exclude={part}&appid={API key}
https://api.openweathermap.org/data/2.5/onecall?lat=34.133500&lon=-118.027020&exclude=current,minutely,daily&appid=f47da300827aa3c1742f1deabeede215
'''

api_key = "f47da300827aa3c1742f1deabeede215"
OWM_Endpoint = "https://api.openweathermap.org/data/2.5/onecall"

'''Locations'''
#Arcadia, CA
# MY_LAT = 34.133500
# MY_LONG = -118.027020
# Mawsynram, Meghalaya State, India
MY_LAT = 25.2975
MY_LONG = 91.5826

parameters = {
    "lat": MY_LAT,
    "lon": MY_LONG,
    "exclude":"current,minutely,daily",
    "appid": api_key,
}

response = requests.get(url=OWM_Endpoint,params=parameters)
response.raise_for_status()
# print(response.status_code)
data_hourly_list = response.json()["hourly"]

'''list of 12 codes'''
# code_12_hrs = []
# for i in range(12):
#     code_12_hrs.append(data_hourly_list[i]["weather"][0]["id"])
# print(code_12_hrs)

'''Will it rain in 12 hours'''
will_rain = False
weather_slice = data_hourly_list[:12]
for hour_data in weather_slice:
    condition_code = hour_data["weather"][0]["id"]
    if condition_code < 700:
        will_rain = True
if will_rain:    
    client = Client(account_sid, auth_token)
    message = client.messages \
                .create(
                     body="Python API practice with Twilio and Openweatherapp. It's raining in Mawsynram, Meghalaya State, India",
                     from_='+18125944188',
                     to='+16262137688'
                 )
    print(message.status)
    print(message.sid)