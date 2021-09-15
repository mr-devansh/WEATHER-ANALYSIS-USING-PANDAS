# with open("weather_data.csv") as data_file:
#     data = data_file.readlines()
#     print(data)

# import csv
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temp = []
#     for row in data:
#         if row[1] != "temp":
#             temp.append(int(row[1]))
# print(temp)

# import pandas
# data = pandas.read_csv("weather_data.csv")
# data_dict = data.to_dict()
# print(data_dict)

# import pandas
# data = pandas.read_csv("weather_data.csv")
# temp_list = data["temp"].to_list()
# average_temp = sum(temp_list)/len(temp_list)
# print(average_temp)
# max_temp = data[data.temp == data.temp.max()]
# print(temp_list)
# print(max_temp)

# import pandas
# data = pandas.read_csv("weather_data.csv")
# monday = data[data.day == "Monday"]
# monday_temp = int(monday.temp)
# monday_temp_F = monday_temp * 9/5 + 32
# print(monday_temp_F)


# import pandas
# data_dict = {
#     "students": ["devansh", "paridhi"],
#     "roll no": [1, 2]
# }
# data = pandas.DataFrame(data_dict)
# data.to_csv("new_data.csv")
# print(data)

