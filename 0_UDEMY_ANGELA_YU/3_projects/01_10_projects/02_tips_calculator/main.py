print("*** Welcome to tip calculator ***")

bill_amount = float(input("What is your bill amount. $"))
tip = int(input("Type Tip amount, 10-15%. "))
people = int(input("How many people bear this bill. "))

tip_percentage = (bill_amount * tip) / 100
result = (bill_amount + tip_percentage) / people

print(f"Each person should pay: ${round(result,2)}")