import random

letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','o','p','q','r','s','t','u','v','x','y','z','A','B','C','D','E','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

numbers = ['0','1','2','3','4','5','6','7','8','9']

symbols = ['!','@','#','$','%','^','&','*','?','<','>']

easy_password = ""
hard_password = ""

user_choose_letter = int(input("How many letters you want password. "))
user_choose_digit = int(input("How many digits you want password. "))
user_choose_symbol = int(input("How many symbols you want password. "))

if user_choose_letter < 0 or user_choose_digit < 0 or user_choose_symbol < 0:
    print("Pleas provide a positive number. At least 1.")
    exit()

for i in range(user_choose_letter):
    easy_password += random.choice(letters)

for i in range(user_choose_digit):
    easy_password += random.choice(numbers)

for i in range(user_choose_symbol):
    easy_password += random.choice(symbols)
    
for i in range(len(easy_password)):
    hard_password += random.choice(easy_password)

print(f"Easy Password- {easy_password}")
print(f"Hard Password- {hard_password}")
