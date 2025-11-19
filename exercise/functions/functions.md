# Learn all about functions by answering the questions below.

<details>
<summary>
1. Basic Function Syntax
</summary>
Problem: Write a function to calculate and return the square of a number.

```python
def square_num(number):
  return number ** 2

result = square_num(3)
print(result)
print(square_num(4))
```

</details>

<details>
<summary>
2. Function with Multiple Parameters
</summary>
Problem: Create a function that takes two numbers as parameters and returns their sum.

```python
def sum (a,b):
  return a + b

print(sum(13,12))
```

</details>

<details>
<summary>
3. Polymorphism in Functions
</summary>
Problem: Write a function multiply that multiplies two numbers, but can also accept and multiply strings.

```python
def multiply(a,b):
  return a * b

print(multiply(5,7))
print(multiply(5,"ab"))
print(multiply("h",8))
```

</details>

<details>
<summary>
4. Function Returning Multiple Values
</summary>
Problem: Create a function that returns both the area and circumference of a circle given its radius.

```python
import math

def circle(radius):
  area = math.pi * radius **2
  circumference = 2 * math.pi * radius
  return area,circumference

area,circumference = circle(3)

print(f"Area- {round(area,2)}, \nCircumference- {round(circumference,2)}")
```

</details>

<details>
<summary>
5. Default Parameter Value
</summary>
Problem: Write a function that greets a user. If no name is provided, it should greet with a default name.

```python
def getting(user_name="Jone"):
  print("Hello", user_name)

getting("Samsuddin")
getting()
```

</details>

<details>
<summary>
6. Lambda Function
</summary>
Problem: Create a lambda function to compute the cube of a number.

```python
cube = lambda x: x ** 3

print(cube(2))
print(cube(4))
print(cube(5))
```

</details>

<details>
<summary>
7. Function with *args
</summary>
Problem: Write a function that takes variable number of arguments and returns their sum.

```python
def sum_with_args(*args):
  return sum(args)

print(sum_with_args(2,3))
print(sum_with_args(3,4,5))
print(sum_with_args(6,7,8,9))
```

</details>

<details>
<summary>
8. Function with **kwargs
</summary>
Problem: Create a function that accepts any number of keyword arguments and prints them in the format key: value.

```python
def student(**kwargs):
  for key,value in kwargs.items():
    print(f"{key} = {value}")

student(name="Samsuddin", roll=12)
student(name="Hayder", roll=1, status="Win the game")
```

</details>

<details>
<summary>
9. Generator Function with yield
</summary>
Problem: Write a generator function that yields even numbers up to a specified limit.

```python
def even_number(limit):
  for i in range(2,limit+1,2):
    yield i

for i in even_number(10):
  print(i)
```

</details>

<details>
<summary>
10. Recursive Function
</summary>
Problem: Create a recursive function to calculate the factorial of a number.

```python
def factorial(n):
  if n == 0:
    return 1
  else:
    return  n * factorial(n-1)

print(factorial(5))
```

</details>
