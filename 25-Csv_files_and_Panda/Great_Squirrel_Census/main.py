

# https://data.cityofnewyork.us/Environment/2018-Central-Park-Squirrel-Census-Squirrel-Data/vfnx-vebw

# Fur Color and Count Dataframe
import pandas
data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

black_squirrels = data[data["Primary Fur Color"] == "Black"]
cinnamon_squirrels = data[data["Primary Fur Color"] == "Cinnamon"]
gray_squirrels = data[data["Primary Fur Color"] == "Gray"]

black_squirrels_count = len(black_squirrels)
cinnamon_squirrels_count = len(cinnamon_squirrels)
gray_squirrels_count = len(gray_squirrels)

# print(f"Black: {black_squirrels_count}")
# print(f"Cinnamon: {cinnamon_squirrels_count}")
# print(f"Gray: {gray_squirrels_count}")

data_dict = {
    "Fur Color":["Black", "Cinnamon", "Gray"],
    "Count":[black_squirrels_count, cinnamon_squirrels_count, gray_squirrels_count],
}
new_data = pandas.DataFrame(data_dict)
new_data.to_csv("fur_color_data.csv")