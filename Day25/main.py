# with open("./weather-data.csv") as weather_data:
#     data_list = weather_data.readlines()
#     print(data_list)

# import csv
# with open("./weather-data.csv") as weather_data:
#     data = csv.reader(weather_data)
#     conditions = []
#     temperature = []
#     all_rows = (list(data))  #if the list the data first then the csv reader works on iterator and it only loop once so that print donot work as we think  => store the list data and then loop those data 
    # print(all_rows)
    # for row in all_rows:
    #     if row[2] != 'condition':
    #         conditions.append(row[2])
    #     # if row[1] != 'temp':
    #         # temperature.append(int(row[1]))
    # print(conditions)
    # print(temperature)
    # print(data)
    # for row in all_rows[1:]: #Skip the header row directly
    #     conditions.append(row[2])
    # print(conditions)

    # This is way the data works over here => watch the weather-data.csv file
    # row = "Sunday" "12" "Rainy"
    # index       value           column
    # 0           Sunday          Day
    # 1           12              temp
    # 2           rainy           condition

import pandas as pd

data = pd.read_csv("weather-data.csv")
# print(data['temp'].to_list()) # to show plain list use to_list()
# print(type(data['temp']))


# data_dict = data.to_dict(orient='records') # If You Want Row-wise Dictionaries:
# print(data_dict)

# temp_list = data['temp'].to_list()
# print(temp_list)

temp_avg = round(data['temp'].mean(),2)
temp_max = data['temp'].max()
print(f"Average: {temp_avg}")
print(f"Maximum: {temp_max}")

# Get the data Columns
# print(data['condition'])
# print(data.condition)

# Get Data in Rows
# print(data[data.day == "Monday"])
# print(data[data.temp == data.temp.max()] )

# sunday = data[data.day == "Sunday"] 
# print(sunday.condition)
# print(sunday.condition.values[0],"Sujan") #print the sunny

# monday = data[data.day == "Monday"]
# # monday_temp = int(monday.temp) #it throw error like TypeError: int() argument must be a string, a bytes-like object or a number, not 'Series'
# monday_temp = int(monday.temp.values[0]) #or monday.temp.iloc[0]
# monday_temp_F = monday_temp * 9/5 + 32
# print(monday_temp_F)

#  Create dataFrame from the scratch
data_dict = {
    "students" : ["Sujan", "Sujata", "Susil"],
    "scores" : [100, 80, 60]
}

data = pd.DataFrame(data_dict)
data.to_csv("new_data.csv", index=False) # if don't want the index column write index=False
print(data)