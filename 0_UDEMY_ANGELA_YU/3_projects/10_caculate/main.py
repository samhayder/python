logo = r"""
 _____________________
|  _________________  |
| | JO           0. | |
| |_________________| |
|  ___ ___ ___   ___  |
| | 7 | 8 | 9 | | + | |
| |___|___|___| |___| |
| | 4 | 5 | 6 | | - | |
| |___|___|___| |___| |
| | 1 | 2 | 3 | | x | |
| |___|___|___| |___| |
| | . | 0 | = | | / | |
| |___|___|___| |___| |
|_____________________|
"""

def add(first_number,last_number):
    return first_number + last_number

def subtract(first_number,last_number):
    return first_number - last_number

def multiply(first_number,last_number):
    return first_number * last_number

def divided(first_number,last_number):
    return first_number / last_number

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divided
}

print(logo)

result = 0
n1 = float(input("\nWhat is the first number? "))

should_continue = True

while should_continue:
    operate = input("\nPick an operation, ('+','-','*','/'): ").strip()
    n2 = float(input("\nWhat is the next number? "))
    result = operations[operate](first_number=n1,last_number=n2)
    print(f"\nResult= {n1} {operate} {n2}= {result}\n")
    
    try_again = input(f"Type 'y' to continue calculate with {result}. type 'n' to start a new calculation. ").strip().lower()
    
    if try_again == "y":
        n1 = result
    else:
        print(f"Goodby. Previous calculate result- {result}")
        result = 0
        should_continue = False

                

        
        
