import pandas

data = pandas.read_csv(r"0_UDEMY_ANGELA_YU/1_lessions/day25_csv_file/Central_Park_Squirrel_Data.csv")
gray_color_count = len(data[data["Primary Fur Color"] == "Gray"])
cinnamon_color_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_color_count = len(data[data["Primary Fur Color"] == "Black"])

# dataframe
data_dict = {
    "Fu Color": ["Gray", "Cinnamon", "Black"],
    "Count": [gray_color_count, cinnamon_color_count, black_color_count]
}
data_frame = pandas.DataFrame(data_dict)
data_frame.to_csv(r"0_UDEMY_ANGELA_YU/1_lessions/day25_csv_file/sequel_count.csv")

