""" Q1. Accept two numbers and print the greatest between them. """
# number1 = float(input("Enter the first number: "))
# number2 = float(input("Enter the second number: "))

# if number1 > number2:
#   print(f" Number1: {number1} is greater than Number2: {number2}")
# elif number2 > number1:
#   print(f" Number2: {number2} is greater than Number1: {number1}")
# else:
#   print("Both number is same.")

""" Q2. Accept the gender from the user as char and print the
respective greeting message
Ex - Good Morning Sir (on the basis of gender) """
# gender = input("Enter your gender: ")
# if gender == "Male" or gender == "male" or gender == "M" or gender == "m":
#   print("Good Morning Sir")
# elif gender == "Female" or gender == "female" or gender == "F" or gender == "f":
#     print("Good Morning Madam")
# else:
#     print("Invalid gender")

""" Q3. Accept an integer and check whether it is an even number
or odd. """
# number = int(input("Enter a number: "))
# if number % 2 == 0:
#   print(f" Number: {number} is an even number")
# else: 
#   print(f" Number: {number} is an odd number")

""" Q4. Accept name and age from the user. Check if the user is a
valid voter or not.
Ex- “hello shery you are a valid voter” """
# name = input("Enter your name: ")
# age = int(input("Enter your age: "))

# if age >=  18:
#   print(f"Hello {name} you are a valid voter")
# else:
#   print(f"Hello {name} you are not a valid voter")

""" Q5. Accept a year and check if it a leap year or not (google to
find out what is a leap year) """

year = int(input("Enter a year: "))

if year % 4 == 0 and (year % 100 == 0 or year % 400 == 0):
  print(f" Year: {year} is a leap year")
else:
  print(f" Year: {year} is not a leap year")


"""Q6. You cna also create if elif ladder using multiple conditions of
elif.
@ For understanding solve this question
@ take the input of temperature in celsiusX
@ Below 0°C → "Freezing Cold b
@ 0°C to 10°C → "Very Cold b
@ 10°C to 20°C → "Cold b
@ 20°C to 30°C → "Pleasant b
@ 30°C to 40°C → "Hot b
@ Above 40°C → "Very Hot " """

temperature = float(input("Enter the temperature in celsius: "))

if temperature < 0:
  print("Freezing Cold")  
elif 0 <= temperature <= 10:
  print("Very Cold")    
elif 10 < temperature <= 20:
  print("Cold")    
elif 20 < temperature <= 30:
  print("Pleasant")
elif 30 < temperature <= 40:
  print("Hot")
else:
  print("Very Hot")





