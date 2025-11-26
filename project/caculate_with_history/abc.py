def calculate():
    user_input = input("calculate. ").strip()
    print(user_input)
    if len(user_input) <= 2:
        print("Invalid.")
        return
    elif len(user_input) >= 5:
        input_split = user_input.split()
        num1 = float(input_split[0])
        operator = input_split[1]
        num2 = float(input_split[2])
    else:
        num1 = float(user_input[0])
        operator = user_input[1]
        num2 = float(user_input[2])
        
    match operator:
        case "+":
            result = num1 + num2
            print("+", result)
        case "-":
            result = num1 - num2
            print("-", result)
        case "*":
            result = num1 * num2
            print("*", result)
        case "/":
            result = num1 / num2
            print("/", result)
        case "%":
            result = num1 % num2
            print("%", result)
        case _:
            print("Invalid operation.")

calculate()