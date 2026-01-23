import pandas

# read data from CSV file into a dataframe
csv_file = pandas.read_csv("3_pandas/file/sales_data_sample.csv", encoding="latin1")

# read data from Excel file into a dataframe
excel_file = pandas.read_excel("3_pandas/file/SampleSuperstore.xlsx")

# read data from JSON file into a dataframe 
json_file = pandas.read_json("3_pandas/file/sample_Data.json")

# print(csv_file)
# print(excel_file)
print(json_file)


# link = https://www.youtube.com/watch?v=0T9qhK5wBqI

