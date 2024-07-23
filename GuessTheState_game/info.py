"""

data = pandas.read_csv("weather_data.csv")
print(data[data.temp == data["temp"].max()]) # Getting the row who mets the condition
"""
import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20240723.csv")



colors = data["Primary Fur Color"].to_list()
gray_squirrels_count = len(data[data["Primary Fur Color"] == "Gray"])
red_squirrels_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrels_count = len(data[data["Primary Fur Color"] == "black"])

squirrel_dict = {
    'Fur Color': ["grey", "red", "black"],
    'Count': [gray_squirrels_count, red_squirrels_count, black_squirrels_count],
}
squirrel_count = pandas.DataFrame(squirrel_dict).to_csv("squirrel_count.csv")

