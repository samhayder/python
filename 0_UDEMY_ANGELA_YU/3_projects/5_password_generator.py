#Easy Version-> lettersymbolrumber(abc*&^236)
#Hard Version-> Random (a*c2^b2&)

import random

letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','o','p','q','r','s','t','u','v','x','y','z','A','B','C','D','E','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
numbers = ['0','1','2','3','4','5','6','7','8','9']
symbols = ['!','@','#','$','%','^','&','*','?','<','>']

print("Welcome to the PyPassword Generator!")
require_letter = int(input("How many letters would you like in your password?\n"))
require_number = int(input("How many numbers would you like in your password?\n"))
require_symbol = int(input("How many symbol would you like in your password?\n"))

password = ""
hard_password = ""

for char in range(1, require_letter + 1):
    password += random.choice(letters)

for char in range(1, require_number + 1):
    password += random.choice(numbers)

for char in range(1, require_symbol + 1):
    password += random.choice(symbols)

for char in password:
    hard_password += random.choice(password)
    
print("Your Easy password- ",password)
print("Your Hard password- ",hard_password)

