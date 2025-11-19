# Questions on Conditionals

<details>
<summary>1. Age Group Categorization
</summary>
Problem: Classify a person's age group: Child (0-13), Teenager (13-19), Adult (20-59), Senior (60+).

```python
age = int(input("Type your age. "))

if age < 0:
  print("Please provide a valid integer number.")
elif age < 13:
  print("Child")
elif age < 20:
  print("Teenager")
elif age < 60:
  print("Adult")
else:
  print("Senior")
```

</details>

<details>
<summary>2. Movie Ticket Pricing
</summary>
Problem: Movie tickets are priced based on age: $12 for adults (18 and over), $8 for children. Everyone gets a $2 discount on Wednesday.

```python
age = int(input("Type your age. "))
day = input("Write Today name. ")
price = 12.0 if age >= 18 else 8.0

if day == "Wednesday":
  price -= 2
  print(f"Movie ticket price ${price}")
else:
  print(f"Movie ticket price ${price}")

```

</details>

<details>
<summary>3. Grade Calculator 
</summary>
Problem: Assign a letter grade based on a student's score: A (90-100), B(80-89), C(70-79), D(60-69), F(below 60).

```python
score = int(input("Type your score. "))

if score >= 101:
  print("Overloading...")
  exit()

if score < 60:
  print(f"{score} Grade is: F")
elif score < 70:
  print(f"{score} Grade is: D")
elif score < 80:
  print(f"{score} Grade is: C")
elif score < 90:
  print(f"{score} Grade is: B")
else:
  print(f"{score} Grade is: A")
```

</details>

<details>
<summary>4. Fruit Ripeness Checker 
</summary>
Problem: Determine if a fruit is ripe, overripe, or unripe based on its color. (e.g./ Banana:Green = Unripe, Yellow- Ripe, Brown- Overripe)

```python
fruit_color = input("Type your fruit color. ")

if fruit_color == "green":
  fruit_cond = "Unripe"
elif fruit_color == "yellow":
  fruit_cond = "Ripe"
elif fruit_color == "brown":
  fruit_cond = "Overripe"
else:
  fruit_cond = "Don't match color."

print(f"Fruit Condition is {fruit_cond}")
```

</details>

<details>
<summary>5. Weather Activity Suggestion
</summary>
Problem: Suggest an activity based on the weather (e.g., Sunny - Go far a walk, Rain - Read a book, Snowy - Build snowman).

```python
weather_info = input("Type weather information. ")
weather = weather_info.lower()

if weather == "sunny":
  print("Go far a walk.")
elif weather == "rain":
  print("Read a Book.")
elif weather == "snowy":
  print("Build snowman.")
else:
  print("Provide right information.")

```

</details>

<details>
<summary>6. Transportation Mode Selection
</summary>
Problem: Choose a mode of transportation based on the distance (e.g., <3km: Walk, 3-15km: Bike, >15km: Car)

```python
distance = int(input("Type your distance in km. "))
transport = ""

if distance < 0:
  print("Invalid distance.")
  exit()

if distance < 4:
  transport = "Walk"
elif distance < 16:
  transport = "Bike"
else:
  transport = "Car"

print(f"{distance}km so choose- {transport}")
```

</details>

<details>
<summary>7. coffee Customization
</summary>
Problem: Customize a coffee order: "Small", "Medium" or "Large" with an option for "Extra short" of espresso.

```python
order_size = input("Select your order size. ")
order = order_size.lower()
extra_short = True

if extra_short:
  order+= " Coffee with Extra Short"
else:
  order+= " Coffee"

print(f"Order: {order.capitalize()}")
```

</details>

<details>
<summary>8. Password Strength Checker
</summary>
Problem: Check if a password is "Weak", "Medium", or "Strong". Criteria: <6 chars (Weak), 6-10 chars (Medium), > 10 chars (Strong)

```python
password_inp = input("Type your password. ")
password = len(password_inp)
criteria = ""

if password <= 6:
  criteria = "Weak"
elif password <= 10:
  criteria = "Medium"
else:
  criteria = "Strong"

print(f"{password_inp} is {criteria}")
```

</details>

<details>
<summary>9. Leap Year Checker 
</summary>
Problem: Determine if a year is a leap year. (Leap years are divisible by 4, but not 100 unless also divisible by 400).

```python
year = 300

if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
  print(year, "Leap Year.")
else:
  print(year, "Not Leap Year.")
```

</details>

<details>
<summary>10. Pet Food Recommendation
</summary>
Problem: Recommend a type of pet food based on the pet's species and age. (e.g., Dog: <2 years- Puppy food, Cat: >5 years- Senior cat food).

```python
dog_age = int(input("Type your dog age. "))

if dog_age <= 2:
  print("Puppy Food")
else:
  print("Senior Food")
```

</details>
