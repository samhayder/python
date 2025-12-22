import random
from art import logo

print(logo)

user_cards = []
computer_cards = []

def deal_cards():
    cards = [11,2,3,4,5,6,7,8,9,10,10,10]
    card = random.choice(cards)
    return card

 
def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
        
    return sum(cards)

for _ in range(2):
    user_cards.append(deal_cards())
    computer_cards.append(deal_cards())

is_game_over = False

while not is_game_over:
    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)

    print(f"Your cards: {user_cards}, Current score: {user_score}")
    print(f"Computer first card: {computer_cards[0]}")

    if user_score == 0 or computer_score == 0 or user_score > 21:
        print("Game over.")
        is_game_over = True
    else:
        user_should_deal = input("Type 'y' to get another card, type 'n' to pass. ").lower()
        
        if user_should_deal == 'y':
            user_cards.append(deal_cards())
        else:
            print("Goodby.")
            is_game_over = True