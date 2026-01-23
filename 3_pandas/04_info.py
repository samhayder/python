""" 1- Columns, Rows?
2- What type of data?
3- Missing data?

info()  ==> Method

1- number of rows and columns
2- column name 
3- int64 float64 object 
4- non null counts
5- memory usage of the data frame """
import pandas

df = pandas.read_csv("3_pandas/file/sales_data_sample.csv", encoding="latin1")

print(df.info())