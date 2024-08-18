# with open("./weather-data.csv") as weather_data:
#     data_list = weather_data.readlines()
#     print(data_list)

# import csv
# with open("./weather-data.csv") as weather_data:
#     data = csv.reader(weather_data)
#     temperature = []
#     for row in data:
#         if row[1] != 'temp':
#             temperature.append(int(row[1]))
#     print(temperature)
    # print(data)

import pandas as pd

data = pd.read_csv("weather-data.csv")
# print(data['temp'])
# print(type(data['temp']))


# data_dict = data.to_dict()
# print(data_dict)

# temp_list = data['temp'].to_list()
# print(temp_list)

temp_avg = round(data['temp'].mean(),2)
temp_max = data['temp'].max()
# print(f"Average: {temp_avg}")
# print(f"Maximum: {temp_max}")

# Get the data Columns
# print(data['condition'])
# print(data.condition)

# Get Data in Rows
# print(data[data.day == "Monday"])
# print(data[data.temp == data.temp.max()] )

sunday = data[data.day == "Sunday"] 
# print(sunday.condition)

monday = data[data.day == "Monday"]
monday_temp = int(monday.temp)
monday_temp_F = monday_temp * 9/5 + 32
# print(monday_temp_F)

#  Create dataFrame from the scratch
data_dict = {
    "students" : ["Sujan", "Suajta", "Susil"],
    "scores" : [100, 80, 60]
}

data = pd.DataFrame(data_dict)
data.to_csv("new_data.csv")
print(data)