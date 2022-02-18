
import requests
from datetime import date, datetime

#Bearer Token Authentication
bearer_headers = {
"Authorization": "afe4therbearertesttoken"
}


GENDER = "male"
WEIGHT_KG = 85.3
HEIGHT_CM = 176
AGE = 25

nutritionix_APP_ID = "0a10f0f1"
nutritionix_API_KEY = "18261b66e1c62a72b5674daeb3690169"
exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

exercise_text = input("Tell me which exercises you did: ")

nutritionix_headers = {
    "x-app-id": nutritionix_APP_ID,
    "x-app-key": nutritionix_API_KEY,
}

parameters = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE,
}

response = requests.post(url=exercise_endpoint, json=parameters,headers=nutritionix_headers)
result = response.json()
# print(result)


'''Sheety and Google sheets'''
'''https://docs.google.com/spreadsheets/d/1xztl70TpvejXpMLL7wclDsPMm3KDt_vR2S3pmFncOcY/edit#gid=0'''

today_date = datetime.now().strftime("%d%m%y")
now_time = datetime.now().strftime("%X")

sheety_username = "1da9576c220c6df09ab7cf61d9926a2d"
project_name = "pythonWorkoutTracker"
sheet_name = "workouts"
# https://api.sheety.co/username/projectName/sheetName
sheety_endpoint = f"https://api.sheety.co/{sheety_username}/{project_name}/{sheet_name}"

for exercise in result["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

sheety_response = requests.post(url=sheety_endpoint,json=sheet_inputs, headers=bearer_headers)
print(sheety_response.text)
