import pandas

df = pandas.read_json("3_pandas/file/sample_Data.json")

# print first 10 rows in data
print("print first 10 rows in data")
print(df.head(10))

# print last 10 rows in data
print("print last 10 rows in data")
print(df.tail(10))