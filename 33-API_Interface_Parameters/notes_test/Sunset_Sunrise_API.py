
'''
https://sunrise-sunset.org/api
https://api.sunrise-sunset.org/json
https://www.latlong.net/
'''

import requests
from datetime import datetime

MY_LAT = 34.133500
MY_LNG = -118.027020
'''https://api.sunrise-sunset.org/json?lat=34.133499&lng=-118.027023'''

parameters = {
    "lat": MY_LAT,
    "lng": MY_LNG,
    "formatted": 0,
}
response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data_json = response.json()
sunrise = data_json["results"]["sunrise"]
sunset = data_json["results"]["sunset"]

sunrise_hr = sunrise.split("T")[1].split(":")[0]
sunset_hr = sunset.split("T")[1].split(":")[0]

print(f"Sunrise: {sunrise}")
print(f"Sunset: {sunset}")

# time_now = datetime.now()
# print(time_now)