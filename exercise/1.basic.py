""" Q1. Write a Python program to swap two variables. """
# a = 10
# b = a


""" Q2. Take user input and display it back to the user. """
# userInput = input("Write your name.")


""" Q3. Write a program to check if a number is even or odd. """
# number = int(input("Type a number. To check odd or even. ->" ))

# if number % 2 ==0:
#   print(f"{number} is even number")
# else:
#   print(f"{number} is odd number")


""" Q4. Create a program that prints the multiplication table of a given number. """
# number = int(input("Type a number. To print multiplication table.-> " ))

# for i in range(1,11,1):
#   print(f"{number} x {i} = {number*i}")


""" Q5. Write a program to find the largest of three numbers. """
# firstNum = 8
# secondNum = 10
# thirdNum = 9

# if firstNum > secondNum and firstNum > thirdNum:
#   print(f"{firstNum} First number is largest")
# elif secondNum > firstNum and secondNum > thirdNum:
#   print(f"{secondNum} Second number is largest")
# else:
#   print(f"{thirdNum} Third number is largest")


""" Q6. Convert temperature from Celsius to Fahrenheit. """
# celsius = float(input("Type celsius to convert fahrenheit.-> "))

# print(f"{celsius} celsius to convert fahrenheit - {celsius*1.8 + 32}")


""" Q7. Write a program to calculate the factorial of a number using a loop. """
# number = int(input("Type a number. To calculate the factorial number.-> " ))
# factorial = 1

# for i in range(number,0,-1):
#   factorial *= i
# print(f"{number} the factorial is {factorial}")


""" Q8. Create a program to count the number of vowels in a string. """
# str = input("Tye sentence to count the vowels. ")
# vowels = "AEIOUaeiou"
# count = 0

# for i in str:
#   if i in vowels:
#     count += 1
# print(count)


""" Q9. Write a Python script to reverse a given string. """
# str = input("Tye sentence to reverse this. ")
# revStr = " "

# for i in range(len(str)-1,-1,-1):
#  revStr += str[i]

# print(revStr)


""" Q10. Check if a number is a palindrome. """
# number = int(input(Type number. To check is palindrome or not. ))
# copyNumber = number
# palindrome = 0

# while number > 0:
#   palindrome =  palindrome * 10 + number % 10
#   number = number // 10

# if copyNumber == palindrome:
#   print("Palindrome number")
# else:
#   print("Not palindrome number")


""" Q11. Write a program to find the sum of first N natural numbers. """
# number = int(input("Type number. To sum first natural number. "))

# def natural_number (number):
#   sum = 0

#   for i in range(1,number + 1):
#     sum += i
  
#   print(f"First natural number sum is {sum}")

# natural_number(number)


""" Q12. Create a number guessing game. """
# number = int()

# def guessing_number_game (number):
#   import random
#   random_number = random.randint(1,11)
#   tries = 3
  
#   for i in range(tries):
#     number = int(input("Guessing a number. "))
  
#     if random_number == number:
#       print("Congratulation! You win.")

#     elif random_number > number:
#       print("Ohh. Try little more upper.")
#       tries -= 1
    
#     elif random_number < number:
#       print("Ohh. Try little more down.")
#       tries -= 1
    
#     if tries == 0:
#       print("Sorry. Your Try limit finish. Start again...")
#       return
  
# guessing_number_game(number)

""" Q13. Write a program to print all prime numbers between 1 and 100. """

def prime_number(number):
  
  for i in range(2, int(number**0.5)+1):
    if number%i == 0:
      print(number)
    else:
      print(number)
      
prime_number(100)

""" Q14. Check if a given year is a leap year or not. """
# def check_leap_year(year):
#   if year % 100 == 0 or (year % 400 == 0 or year % 4 == 0):
#     print(f"{year} is Leap Year")
  
#   else:
#     print(f"{year} is not Leap Year")
    
# check_leap_year(2000)
# check_leap_year(2025)
    

""" Q15. Create a program to print the Fibonacci series up to N terms. """

""" Q16. Write a program to find the GCD of two numbers. """

""" Q17. Write a program to find the LCM of two numbers. """

""" Q18. Check whether a character is a vowel or consonant. """

""" Q19. Write a program to calculate the sum of digits of a number. """


""" Q20. Create a program to find the second largest number in a list. """

""" Q21. Write a program to count the number of digits in an integer. """

""" Q22. Create a program to print all Armstrong numbers between 1 to 1000. """

""" Q23. Write a Python program to print a pattern of stars in a triangle. """

""" Q24. Create a calculator app using if-else. """

""" Q25. Write a program to display the ASCII value of a character. """

""" Q26. Convert a decimal number to binary using loops. """


""" Q27. Create a program to find the square root of a number. """     

""" Q28. Write a program to find the sum of all even numbers in a list. """

""" Q29. Create a program to check whether a number is prime or not. """

""" Q30. Write a program to display the cube of the number up to an integer. """