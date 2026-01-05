students_details = {
    "name": "Samsuddin",
    "age": 35
}

# Add Items in dictionary
students_details["roll"] = 125
students_details["group"] = "Arts"

# Edit dictionary
students_details["group"] = "Business Studies"

# print dictionary
print(students_details)

# Loop through in dictionary
for key in students_details:
    print(f"{key}= {students_details[key]}")