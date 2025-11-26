HISTORY_FILE = "history.txt"


def calculate_history():
    try:
        file = open(HISTORY_FILE, 'r')
        lines = file.readlines()
        
        if len(lines) == 0:
            print("Calculation History not enters. Add calculation.")
        else:
            for line in reversed(lines):
            
                print(line.strip())  
            print("*"*50)
        file.close()
    
    except FileNotFoundError:
        print("File don't found.")

def clear_history():
    with open(HISTORY_FILE,'w') as fs:
        fs.close()
    print("Clear all calculation history.")
    
def save_calculation(equation,result):
    file = open(HISTORY_FILE,'a')
    file.write(f"{equation} = {str(result)}\n")
    file.close()

def calculation(user_input):
    parts = user_input.split()
    number1 = float(parts[0])
    operator = parts[1]
    number2 = float(parts[2])
    
    if operator == "+":
        result = number1 + number2
    elif operator == "-":
        result = number1 - number2
    elif operator == "*":
        result = number1 * number2
    elif operator == "/":
        if number2 == 0:
            print(f"0 is not divided.")
            return
        else:
            result = number1 - number2
    elif operator == "%":
        result = (number1 * number2) / 100
        
    """ if int(result) == result:
        result = int(result) """
    print(f"Result:- {user_input} = {result}")
    
    save_calculation(user_input,result)

def main():
    while True:
        user_input = input("Calculation, e.g(8 + 2) or command- history, clear, exit. ").strip().lower()
        
        if user_input == "exit":
            print("Goodby! The program is closed.")
            break
        elif len(user_input) <= 3:
            print("Invalid expression. Try e.g (8 + 2)")
            break
        elif user_input == "history":
            calculate_history()
        elif user_input == "clear":
            clear_history()
        else:
            calculation(user_input)
        
if __name__ == "__main__":
    main()
            
        