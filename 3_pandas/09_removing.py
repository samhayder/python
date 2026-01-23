import pandas

seul_machinary = {
    "Worker_Name": ["Chondon", "Samim", "Salauddin", "Johir", "Murad", "Selim", "Shahin", "Rohim", "Samsuddin"],
    "Age": [40,38,55,61,41,47,22,50,36],
    "Salary": [23000,21000,16500,15000,18000,20000,20000,20000,24000],
    "Performance": [78,85,59,27,36,48,68,72,73]
}

df = pandas.DataFrame(seul_machinary)

df.drop(columns=["Performance"], inplace=True)
print("Remove column\n", df)