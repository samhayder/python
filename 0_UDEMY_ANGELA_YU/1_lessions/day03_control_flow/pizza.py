'''Small pizza (S): $15
Medium pizza (M): $20
Large pizza (L): $25
Add pepperoni for small pizza (Y or N): +$2
Add pepperoni for medium or large pizza (Y or N): +$3
Add extra cheese for any size pizza (Y or N): +$1'''

pizza_size = input("Type pizza size: S, M or L ").strip().lower()
extra_pepperoni = input("Add extra pepperoni Y for yes or N for no. ").strip().lower()
extra_cheese = input("Add extra cheese- $1. Y for yes or N for no. ").strip().lower()

pizza_price = 0
pepperoni = 0
cheese = 1
bill = 0

if pizza_size == "l":
    pizza_price = 25
    bill = pizza_price
    if extra_pepperoni == "y":
        pepperoni = 3
        bill += pepperoni
    
    if extra_cheese == "y":
        bill += cheese
    
    print(f"Pizza size {pizza_size}- price ${bill}")

elif pizza_size == "m":
    pizza_price = 20
    bill = pizza_price
    if extra_pepperoni == "y":
        pepperoni = 3
        bill += pepperoni
    
    if extra_cheese == "y":
        bill += cheese
    
    print(f"Pizza size {pizza_size}- price ${bill}")
    
else:
    pizza_price = 15
    bill = pizza_price
    if extra_pepperoni == "y":
        pepperoni = 2
        bill += pepperoni
    
    if extra_cheese == "y":
        bill += cheese
    
    print(f"Pizza size S- price ${bill}")   
