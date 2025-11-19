# Loops in Python

<details>
<summary>
1. Counting Positive Numbers
</summary>
Problem: Given a list of numbers, count how many are positive.

```python
numbers = [1,- 2, 3, -4, 5, 6, -7, -8, 9, 10]
count = 0

for i in numbers:
  print(i)
  if i > 0:
    count += 1

print("Positive number is ", count)
```

</details>

<details>
<summary>
2. Sum of Even Numbers
</summary>
Problem: Calculate the sum of even numbers up to a given number n.

```python
number = int(input("Given a integer number. "))
sum = 0

for i in range(1,number+1):
  if i % 2 == 0:
    sum += i

print(number,"- sum is= ", sum)
```

</details>

<details>
<summary>
3. Multiplication Table Printer
</summary>
Problem: Print the multiplication table for a given number up to 10, but skip the fifth iteration.

```python
number = int(input("Given a number. "))

for i in range(1,11):
  if i == 5:
    continue
  print(f"{number} x {i} = {number*i}")
```

</details>

<details>
<summary>
4. Reverse a String
</summary>
Problem: Reverse a string using a loop.

```python
str = input("Given string. ")
reverse_str = ""

for char in str:
  reverse_str = char + reverse_str

print(reverse_str)
```

</details>

<details>
<summary>
5. Find the First Non-Repeated Character
</summary>
Problem: Given a string, find the first non-repeated character.

```python
input_str = "referral"

for char in input_str:
  if input_str.count(char) == 1:
    print("Non-Repeated Character is- ", char)
    break
```

</details>

<details>
<summary>
6. Factorial Calculator
</summary>
Problem: Compute the factorial of a number using a while loop.

```python
factorial_number = 5
factorial = 1

while factorial_number > 0:
  factorial *= factorial_number
  factorial_number -= 1

print(factorial)
```

</details>

<details>
<summary>
7. Validate Input
</summary>
Problem: Keep asking the user for input until they enter a number between 1 and 10.

```python
while True:
  user_input = int(input("Enter a number 1 -10. "))

  if 1 <= user_input <= 10:
    print("Matching number.")
    break


```

</details>

<details>
<summary>
8. Prime Number Checker
</summary>
Problem: Check if a number is prime.

```python
input_number = 11
is_prime = True

if input_number > 0:
  for num in range(2,input_number):
    if input_number % num == 0:
      is_prime = False

print(is_prime)
```

</details>

<details>
<summary>
9. List Uniqueness Checker
</summary>
Problem: Check if all elements in a list are unique. If a duplicate is found, exit the loop and print the duplicate.

```python
items = ["apple", "banana", "orange", "apple", "mango"]
unique_items = set()

for item in items:
  if item in unique_items:
    print("Duplicate item is- ", item)
    break
  else:
    unique_items.add(item)

print(unique_items)

```

</details>

<details>
<summary>
10. Exponential Backoff
</summary>
Problem: Implement an exponential backoff strategy that doubles the wait time between retries, starting from 1 second, but stops after 5 retries.

```python
import time

wait_time = 1
max_retries = 3
attempt = 0

while attempt < max_retries:
  print(f"Attempt: {attempt+1}, Wait Time: {wait_time}s")
  time.sleep(wait_time)
  wait_time *= 2
  attempt += 1
```

</details>
