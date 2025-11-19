""" Data Types """

# Integers
number = 28
print(number )
print(type(number) )

# Floats
mark = 2.5
divided = mark / number
print(mark)
print(type(mark))
print(divided)
print(type(divided))

# Complex
complex = 10j
print(complex)
print(type(complex))

# Booleans

# Strings

""" student = input("Enter your name: ")
stu_age = int(input("Enter your age: "))
print(f"MY name is {student} and my age is {stu_age}") """


print( 20.1 > 20.0)

# function
def palindrome(str):
  revStr = ""

  for i in range(len(str)-1,-1,-1):
    revStr += str[i]

  if revStr == str:
    print(f"{str} is a palindrome")
  else:
    print(f"{str} is not a palindrome")


palindrome("MADAM")
palindrome("Madam")
palindrome("SiR")





