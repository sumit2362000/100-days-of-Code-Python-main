
# csv = comma separated values

# with open("weather_data.csv", mode='r') as data:
#     weather_data = data.readlines()
# print(weather_data)

'''in built csv library'''
# import csv
# with open("weather_data.csv", mode='r') as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != 'temp':
#             temperatures.append(int(row[1]))
#     print(temperatures)

'''Using pandas'''
import pandas
data = pandas.read_csv("weather_data.csv")
# print(type(data)) # <class 'pandas.core.frame.DataFrame'>
# print(data)
# print(type(data["temp"])) # <class 'pandas.core.series.Series'>
# print(data["temp"])

# https://pandas.pydata.org/pandas-docs/stable/reference/index.html
# Series and Dataframe
data_dict = data.to_dict()
# print(data_dict)
temp_list = data["temp"].tolist()
# print(temp_list)

'''python calculate average temperature'''
# average_temp = sum(temp_list)/len(temp_list)
# formatted_average_temp = "{:.2f}".format(average_temp)
# print(f"Average Temperature: {formatted_average_temp}")
'''mean using Pandas'''
# panda_temp_average = "{:.2f}".format(data["temp"].mean()) # data["temp"].mean()
# print(f"Average Temperature using built in Panda method: {panda_temp_average}")
'''max using Pandas'''
# max_temp = data["temp"].max()
# print(f"Max value: {max_temp}")

'''Get data in columns'''
# print(data["condition"])
# print(data.condition)

'''Get Data in Row'''
# print({data[data.day == "Monday"]})

'''Row data of highest temp'''
# max_temp = data.temp.max()
# print(data[data.temp == max_temp])

'''Convert monday's Celsius to Farenheit'''
# monday = data[data.day == "Monday"]
# monday_C_Temp = int(monday.temp)
# monday_F_Temp = monday_C_Temp * (9/5) + 32
# print(f"Monday Farenheit Temp: {monday_F_Temp} F")

'''Create a data frame from scratch'''
# data_dict = {
#     "students": ["Amy", "James", "Angela"],
#     "scores": [76,56,65],
# }
# data = pandas.DataFrame(data_dict)
# print(data)
# data.to_csv("new_data.csv")
