""" 
NaN (Not a Number)
None (for object data type)

Method ==> isnull()
True - Nan is missing
False - value is present
"""

import pandas

seul_machinary = {
    "Worker_Name": ["Chondon", "Samim", "Salauddin", None, "Murad", "Selim", "Shahin", "Rohim", "Samsuddin"],
    "Age": [40,38,55,None,41,47,22,50,36],
    "Salary": [23000,21000,16500,None,18000,20000,20000,20000,24000],
    "Performance": [78,85,59,None,36,48,68,72,73]
}

df = pandas.DataFrame(seul_machinary)

# check data missing
print(df.isnull())

# Count missing data
print(df.isnull().sum())

# #Handling Missing Data

# Remove missing data
df.dropna(axis=0, inplace=True)

# Fill missing data
df.fillna(value=0,inplace=True)
df["Age"].fillna(value=df["Age"].mean(), inplace=True)
print(df)
