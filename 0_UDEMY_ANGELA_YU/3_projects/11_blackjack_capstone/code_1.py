import random

cards = [11,2,3,4,5,6,7,8,9,10,10,10]
your_cards = []
computer_cards = []
your_cards_sum = 0
computer_cards_sum = 0


for card in cards:
    if len(your_cards) < 2:
        your_cards.append(random.choice(cards))
        your_cards_sum = sum(your_cards)
    elif len(computer_cards) < 1:
        computer_cards.append(random.choice(cards))
        computer_cards_sum = sum(computer_cards)
    

print(f"\nYour cards is- {your_cards}, Total point: {your_cards_sum}")
print(f"Computer cards is- {computer_cards}, Total point: {computer_cards_sum}\n")

should_continue = True

while should_continue:
    add_card = input("Add another card. Type 'y' or pass 'n'. ").lower()

    if add_card == 'y':
        your_cards.append(random.choice(cards))
        computer_cards.append(random.choice(cards))
        your_cards_sum = sum(your_cards)
        computer_cards_sum = sum(computer_cards)
        print(f"\nYour cards is- {your_cards}, Total point: {your_cards_sum}")
        print(f"Computer cards is- {computer_cards}, Total point: {computer_cards_sum}\n")
        
        if your_cards_sum > 21:
            print(f"Lose! Your point- {your_cards_sum} over 21.")
            should_continue = False
        
    else:
        print("Goodby.")
        should_continue = False
