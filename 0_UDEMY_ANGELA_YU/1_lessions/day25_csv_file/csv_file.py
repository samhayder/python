import csv

with open(r"0_UDEMY_ANGELA_YU/1_lessions/day25_csv_file/weather_data.csv") as data_file:
    data_list = csv.reader(data_file)
    temperature = []
    for data in data_list:
        if data[1] != "temp":
            temperature.append(int(data[1]))
    print(temperature)