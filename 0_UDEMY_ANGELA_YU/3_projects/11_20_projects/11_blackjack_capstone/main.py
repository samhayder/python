import random
from art import logo

def random_card():
    cards = [11,2,3,4,5,6,7,8,9,10,10,10]
    card = random.choice(cards)
    return card

def calculate_card(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
        
    return sum(cards)

def compare(s_user,s_computer):
    if s_user == 0 and s_computer == 0:
        print("***** Blackjack *****\n")
    elif s_user > s_computer and s_user < 21:
        print("***** You Win *****\n")
    elif s_computer > s_user and s_computer < 21:
        print("***** Computer Win *****\n")
    elif s_user == s_computer:
        print("***** Draw *****")
    else:
        print("***** You Lose *****\n")


def play_game():
    
    print(logo)
    
    user = []
    computer = []
    user_sum = 0
    computer_sum = 0
    is_game = True

    for _ in range(2):
        user.append(random_card())
        computer.append(random_card())

    while is_game:
        user_sum = calculate_card(user)
        computer_sum = calculate_card(computer)
        
        print(f"\nYour cards- {user}, Current score- {user_sum}")
        print(f"Computer first card- {computer[0]}, Current score: {computer[0]}\n")
        
        if user_sum == 0 or computer_sum == 0 or user_sum > 21:
            is_game = False
        else:
            add_card = input("Type 'y' add another card, type 'n' to pass. ").lower()
        
            if add_card == 'y':
                user.append(random_card())
            else:
                is_game = False

    while computer_sum != 0 and computer_sum < 17:
        computer.append(random_card())
        computer_sum = calculate_card(computer)

    print(f"\nYour Final Hand- {user}, Current score- {user_sum}")
    print(f"Computer Final Hand- {computer}, Current score: {computer_sum}\n")
    compare(user_sum,computer_sum)
    
while input("Do you went play game. Type 'y' to play or 'n' to exit: ").lower() == 'y':
    play_game()