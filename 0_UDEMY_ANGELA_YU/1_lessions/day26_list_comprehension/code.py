import random
# List Comprehension
#new_list = [new_item for item in list]
numbers = [1,2,3,4]
new_list = [n+1 for n in numbers]
print(new_list)

name = "Samsuddin"
new_name = [letter for letter in name]
print(new_name)

double_num = [n*2 for n in range(1,5)]
print(double_num)

name_list = ["Samsuddin", "Hayder", "Ridoy", "Salman", "Yasin", "Suria", "Jannat"]
check_name = [name.upper() for name in name_list if len(name) > 5]
print(check_name)

# Dictionary comprehension
student_score = {student:random.randint(1,100) for student in name_list}
passed_student = {student:score for (student,score) in student_score.items() if score >= 33}
print(passed_student)

# exercise 1
sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
sentence_list = sentence.split(" ")
result = {key:len(key) for key in sentence_list}
print(result)

# exercise 2
weather_c = {"Monday": 12, "Tuesday": 14, "Wednesday": 15, "Thursday": 14, "Friday": 21, "Saturday": 22, "Sunday": 24}

weather_f = {day:(celsius*9/5)+32 for (day,celsius) in weather_c.items()}

print(weather_f)