""" 1. Accept an integer and Print hello world n times """
# number = int(input("Type a integer number. To print n times:- "))

# for i in range(1,number + 1):
#   print(f"Hello World - {i}")


""" 2. Print natural number up to n """
# number = int(input("Type a number. To print natural number:- "))

# if number < 0 :
#   print("Please type positive integer number.")

# for i in range(number + 1):
#   print(f"{i} is natural number to n-{number}.")


""" 3. Reverse for loop. Print n to 1 """
# number = int(input("Type number. To print reverse number:- "))

# for i in range(number, -1,-1):
#   print(f"{i}")


""" 4. Take a number as input and print its table """
# number = int(input("Type a number. To print multiplications in table:- "))

# for i in range(1, 11, 1):
#   print(f"{number} x {i} = {number * i}")

""" 5. Sum up to n terms """
# number = int(input("Type a number. To sum n terms:- "))
# sum = 0

# for i in range(number+1):
#   sum += i

# print(f"{number} total sum is = {sum}")


""" 6. Factorial of a number """
# number = int(input("Type a number. To print factorial number:- "))
# factorial = 1

# for i in range(number,0,-1):
#   factorial *= i
  
# print(factorial)


""" 7. Print the sum of all even & odd numbers in a range
separately """
# number = int(input("Type a number. To sum all even & odd number:- "))
# even = 0
# odd = 0

# for i in range(1, number +1, 1):
#   if i % 2 == 0:
#     even += i
# print(f"{number} total even to sum = {even}")

""" 8. Print all the factors of a number """
# number = int(input("Type a number. To print factors number:- "))

# for i in range(1, number + 1): 
#   if number % i == 0:
#     print(f"Factors numbers are {i}")


""" 9. Accept a number and check if it a perfect number or not. 
      A number whose sum of factors is equal to the number itself
      Ex - 6 = 1, 2, 3"""

# number = int(input("Type a number. To print prefect number:- "))
# sum = 0

# for i in range(1, number):
#   if number % i == 0:
#     sum += i

# if sum == sum:
#   print(f"{number} is the perfect number.")
# else:
#   print(f"{number} is not perfect number.")


""" 10. Check wether the number is prime or not """
# number = int(input("Type a number. To print prime number:- "))
# count = 0

# for i in range(1, number+1):
#   if number % i == 0:
#     count += 1

# if count == 2:
#   print(f"{number} is prime number")
# else:
#   print(f"{number} is not prime number")


""" 11. Reverse a string without using in build functions. """
# str = input("Type word or sentence. To reverse this. ")
# revStr = " "

# for i in range(len(str)-1,-1,-1):
#   revStr += str[i]

# print(revStr)


""" 12. Check string is Palindrome or not """
# str = input("Type text. To check palindrome or not.- ")
# revStr = ""

# for i in range(len(str)-1,-1,-1):
#   revStr += str[i]

# if revStr == str:
#   print("It's palindrome.")
# else:
#   print("It's not palindrome.")

""" 13. Count all letters, digits, and special symbols from a given string
Given: str1 = "P@#yn26at^&i5ve"
Expected Outcome:
Total counts of chars, digits, and symbols
Chars = 8
Digits = 3
Symb= 4 """

# str = "P@#yn26at^&i5ve"
# chars = 0
# digits = 0
# symb = 0

# for i in str:
#   if i.isalpha():
#       chars += 1
#   elif i.isdigit():
#      digits += 1
#   else:
#      symb += 1

# print(f"Chars are {chars}\nDigits are {digits}\nSymbol are {symb}")


""" === While Loops === """
""" 14. Separate each digit of a number and print it on the new line """
# number = int(input("Type a digit. To print new line.- "))

# while number > 0:
#      print(number % 10)

#      number = number // 10


"""  15. Accept a number and print its reverse """
# number = int(input("Type a digit. To print reverse.- "))
# revNum = 0

# while number > 0:
#   revNum = revNum*10 + number % 10
#   number = number // 10

# print(revNum)


"""  16. Accept a number and check if it is a palindromic number (If number and its reverse are equal? """
# number = int(input("Type a digit. To check is palindrome or not.- "))
# copyNumber = number
# revNum = 0

# while number > 0:
#   revNum = revNum * 10 + number % 10
#   number = number // 10

# if copyNumber == revNum:
#   print("It's palindrome number.")
# else:
#   print("It's not palindrome number.")


"""  17. Create a random number guessing game with python. """
import random

number = random.randint(1,10)
tries = 0

while tries < 3:
  guessing = int(input("Guessing a number to check random number.- "))

  if number == guessing:
    print(f"Congratulations! You win the game.")
    tries = 4

  elif tries == 2:
    print("Sorry! Your try limit is finished")
    tries += 1

  elif number > guessing:
    print("Try again. Go a little higher")
    tries += 1

  elif number < guessing:
    print("Try again. Go a little lower")
    tries += 1

