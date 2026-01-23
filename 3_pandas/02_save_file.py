import pandas

data = {
    "Name": ["Samsuddin", "Hayder", "Ridoy"],
    "Age": [33,25,16],
    "City": ["Mirpur", "Banani", "Gulistan"]
}

# read dataframe in own created
df = pandas.DataFrame(data)

# Save dataframe in CSV file
df.to_csv("3_pandas/file/save_dataframe.csv", index=False)

print(df)