import pandas

data = pandas.read_csv("weather_data.csv")

print(data[data.temp == data["temp"].max()]) # Getting the row who mets the condition



