import pandas

data = pandas.read_csv(r"0_UDEMY_ANGELA_YU/1_lessions/day25_csv_file/weather_data.csv")

# convert dictionary
data_dict = data.to_dict()
# convert list
data_list = data["temp"].to_list()
# calculate average in the temperature
temp_avg = sum(data_list) / len(data_list)
# print max value in temp.
temp_max = max(data_list)
# print max value in temp. with whole data
temp_max_data = data[data.temp == max(data.temp)]
# change day temp. celcius into fahrenheit
monday = data[data.day == "Monday"]
monday_celcius = monday.temp
monday_fahrenheit = (monday_celcius * 9/5) + 32

# crate a dataframe in scratch
raw_dict = {
    "students": ["Sams", "yasn", "hayd", "jant"],
    "score": [1,3,5,6]
}
raw_dict_data = pandas.DataFrame(raw_dict)
print(raw_dict_data)



