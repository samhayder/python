import random
from ASCII_art import rock,paper,scissor

game_list = [rock,paper,scissor]
game_radom_choice = random.choice(game_list)
game_over = False

while not game_over:
    user_choice = input("Choose an option. 0-for Rock, 1-for Paper, 2-for Scissor. or Exit. ").strip().lower()
    
    if user_choice == "exit":
        print("Goodby! Exit the game.")
        game_over = True
        
    elif user_choice == "0":
        print("\nYour choice- Rock", game_list[0])
        if game_radom_choice == game_list[2]:
            print("\nComputer choice- Scissor", game_list[2])
            print("**** Result-- You Win ****")
            game_over = True
        elif game_radom_choice == game_list[1]:
            print("\nComputer choice- Scissor", game_list[1])
            print("**** Result-- You Lose ****")
        elif game_radom_choice == game_list[0]:
            print("\nComputer choice- Scissor", game_list[0])
            print("**** Result-- Draw ****")
    
    elif user_choice == "1":
        print("\nYour choice- Paper", game_list[1])
        if game_radom_choice == game_list[0]:
            print("\nComputer choice- Rock", game_list[0])
            print("**** Result-- You Win ****")
            game_over = True
        elif game_radom_choice == game_list[2]:
            print("\nComputer choice- Scissor", game_list[2])
            print("**** Result-- You Lose ****")
        elif game_radom_choice == game_list[1]:
            print("\nComputer choice- Paper", game_list[1])
            print("**** Result-- Draw ****")
            
    elif user_choice == "2":
        print("\nYour choice- Scissor", game_list[2])
        if game_radom_choice == game_list[1]:
            print("\nComputer choice- Paper", game_list[1])
            print("**** Result-- You Win ****")
            game_over = True
        elif game_radom_choice == game_list[0]:
            print("\nComputer choice- Rock", game_list[0])
            print("**** Result-- You Lose ****")
        elif game_radom_choice == game_list[2]:
            print("\nComputer choice- Scissor", game_list[2])
            print("**** Result-- Draw ****")
    
    else:
        print("Invalid Input")
        game_over = True
        