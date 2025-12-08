height = int(input("What is your height? To access rollercoaster game. "))
bill = 12

if height >= 120:
    print("You can access rollercoaster. Enjoy the moment.")
    
    age = int(input("What is your age. To need ticket price. "))
    if age < 13:
        bill = 5
        print("Child ticket price: $5")
    elif age < 19:
        bill = 7
        print("Teenager ticket price: $7")
    else:
        print("Adult ticket Price: $12")
    
    want_photo = input("Do you want to have a photo take $3. Type y for yes or n for no ").strip().lower()
    if want_photo == "y":
        bill += 3
    
    print(f"Your current bill is ${bill}")
else: 
    print("Sorry! This height can't access rollercoaster game. Try next time...")