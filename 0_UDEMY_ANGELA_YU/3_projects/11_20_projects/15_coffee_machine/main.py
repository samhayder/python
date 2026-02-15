from menu_data import MENU

logo = r'''
  ____       __  __             __  __            _     _            
 / ___|___  / _|/ _| ___  ___  |  \/  | __ _  ___| |__ (_)_ __   ___ 
| |   / _ \| |_| |_ / _ \/ _ \ | |\/| |/ _` |/ __| '_ \| | '_ \ / _ \
| |__| (_) |  _|  _|  __/  __/ | |  | | (_| | (__| | | | | | | |  __/
 \____\___/|_| |_|  \___|\___| |_|  |_|\__,_|\___|_| |_|_|_| |_|\___|
'''

resources = {
    'water': 1000,
    'coffee': 120,
    'milk': 250
}

profit = 0

machine_is_on = True

# Add extra resource
def add_resources():
    resources['water'] += int(input("Add Water: "))
    resources['coffee'] += int(input("Add Coffee: "))
    resources['milk'] += int(input("Add Milk: "))

# Show all resource
def show_report():
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Total Earn: ${profit}")

# Check resources sufficient
def check_resources(order_item):
    for item in order_item:
        if order_item[item] >= resources[item]:
            print(f"Sorry that's not enough {item}")
            return False
        else:
            return True

# Collect Coin in user
def collect_coin(order):
    total_money = 0
    print(f"Your selected drink- {order.capitalize()} & bill is- ${MENU[order]['price']}")
    print("Please insert coins.")
    total_money += int(input("How many quarters($0.25)? ")) * 0.25
    total_money += int(input("How many dimes($0.10)? ")) * 0.10
    total_money += int(input("How many nickles($0.05)? ")) * 0.05
    total_money += int(input("How many pennies($0.01)? ")) * 0.01
    
    return round(total_money,2)

# Check Transaction
def check_transaction(order):
    global profit
    money = collect_coin(order)
    drink_price = MENU[order]['price']
    water = MENU[order]['items']['water']
    coffee = MENU[order]['items']['coffee']
    milk = MENU[order]['items']['milk']
    refund_money = money - drink_price
    
    if money > drink_price:
        profit += drink_price
        resources['water'] -= water
        resources['coffee'] -= coffee
        resources['milk'] -= milk
            
        print(f"\nThank You. ☕︎ {order.capitalize()} drink is ready. Money refunded- ${refund_money}")
    else:
        print(f"\nSorry that's not enough money. Money refunded- ${money}")
    
    

while machine_is_on:
    print(logo)
    
    choice = input("\nWhat would you like? (espresso-$1.5/latte-$2.5/cappuccino-$3.0)': ").lower()
    
    if choice == 'off':
        print("Goodby. The coffee machine is off.")
        machine_is_on = False
    elif choice == 'add':
        add_resources()
        show_report()
    elif choice == 'report':
        show_report()
    elif choice == 'espresso' or choice == 'latte' or choice == 'cappuccino':
        drink = MENU[choice]
        if check_resources(drink['items']):
            check_transaction(choice)
        
    else:
        print("Invalid input.")    
        machine_is_on = False