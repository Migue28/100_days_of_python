# with open("weather_data.csv") as weather_data:
#     data = weather_data.readlines()
#
# print(data)
# import csv
#
# temperature = []
# with open("weather_data.csv") as weather_data:
#     data = list(csv.reader(weather_data))
#     for row in data[1:]:
#         temperature.append(int(row[1]))
# print(temperature)

# import pandas as pd
#
# data = pd.read_csv("weather_data.csv")
#
# # Average temperature
# temps = data["temp"]
# average_temp = sum(temps)/len(temps)
# print(temps)
# print(round(average_temp, 2))
# print(f"Average temperature {temps.mean()}")
# print(f"Max temperature {temps.max()}")
# print(data[data.temp == data.temp.max()])

# monday = data[data.day == "Monday"]
# print((monday.temp*1.8) + 32)

# dict_data = {"Names": ["Ed", "Al", "Amy"],
#              "Scores": [45, 94, 24]}
# data = pd.DataFrame(dict_data)
# data.to_csv("new_csv_file.csv")

import pandas as pd

data = pd.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
color_squirrel_list = data["Primary Fur Color"]
color_squirrel_list.value_counts().to_csv("color_squirrel_counter.csv")
