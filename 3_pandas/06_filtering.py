""" 
1- select specific column
2- filter rows
3- combine multiple conditions

1- square brackets
2- boolean conditions

selecting columns
1- a series
2- dataframe multiple columns of data

column = df["column name"]
subset = df[["column1", "column2", "..."]]

filtering rows
boolean indexing

#base on a single condition
filtered_rows = df[df["column] > value]

# combine multiple conditions
filtered_rows = df[(df["column1"] > value) & (df["column2] < value)]
"""

import pandas

seul_machinary = {
    "Worker_Name": ["Chondon", "Samim", "Salauddin", "Johir", "Murad", "Selim", "Shahin", "Rohim", "Samsuddin"],
    "Age": [40,38,55,61,41,47,22,50,36],
    "Salary": [23000,21000,16500,15000,18000,20000,20000,20000,24000],
    "Performance": [78,85,59,27,36,48,68,72,73]
}

# display dataframe
df = pandas.DataFrame(seul_machinary)
print("Display Dataframe\n",df)

# filter single column
single_col = df["Worker_Name"]
print("Filter Single column\n", single_col)

# filter multiple columns
multiple_columns = df[["Worker_Name","Salary"]]
print("Multiple filtering columns\n",multiple_columns)

# condition on single 
single_cond = df[df['Age'] < 31]
print("Condition single column\n",single_cond)

# multiple condition
multiple_cond = df[(df["Salary"] < 18000) | (df["Performance"] > 50)]
print("Multiple condition\n",multiple_cond)