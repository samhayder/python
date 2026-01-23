import pandas

seul_machinary = {
    "Worker Name": ["Chondon", "Samim", "Salauddin", "Johir", "Murad", "Selim", "Shahin", "Rohim", "Samsuddin"],
    "Salary": [23000,21000,16500,15000,18000,20000,20000,20000,24000],
    "Performance": [78,85,59,27,36,48,68,72,73]
}

df = pandas.DataFrame(seul_machinary)

print("Sample Data Frame")
print(df)

print("Describe Statistics")
print(df.describe())
""" Describe Statistics
             Salary  Performance
count      9.000000     9.000000    ==> check missing data
mean   19722.222222    60.666667    ==> Average
std     2884.344717    19.786359    ==> Standard Division (Low/High)
min    15000.000000    27.000000    ==> Minimum Value 
25%    18000.000000    48.000000    ==> First Quarter
50%    20000.000000    68.000000    ==>
75%    21000.000000    73.000000    ==>
max    24000.000000    85.000000    ==> Maximum Value
"""