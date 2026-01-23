import pandas

seul_machinary = {
    "Worker_Name": ["Chondon", "Samim", "Salauddin", "Johir", "Murad", "Selim", "Shahin", "Rohim", "Samsuddin"],
    "Age": [40,38,55,61,41,47,22,50,36],
    "Salary": [23000,21000,16500,15000,18000,20000,20000,20000,24000],
    "Performance": [78,85,59,27,36,48,68,72,73]
}

df = pandas.DataFrame(seul_machinary)

# Adding items with value
df["Bonus"] = df["Salary"] * 0.15
print("Adding Bonus item\n",df)

# Adding value by insert in positionally
df.insert(loc=0,column="Worker_Id",value=[11,12,13,14,15,16,17,18,19])
print("Adding value by insert in positionally\n",df)

filtering_selective_index = df[df["Worker_Id"] == 11]
print(filtering_selective_index)