import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissor = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

while True:
    user_choose = int(input("Do you want to choose  0- for Rock, 1- for Paper, 2- for Scissor\n"))
    game = [rock,paper,scissor]
    computer = random.choice(game)

    if user_choose < 0 and user_choose >= 3:
        print("*"*50+"\nInvalid choose.\n")
        exit()

    if user_choose == 0:
        print(f"You choose: Rock {game[user_choose]}")
        if computer == game[2]:
            print(f"Computer choose: Scissor {computer}")
            print("*"*50+"\nYou Win\n")
            exit()
        elif computer == game[0]:
            print(f"Computer choose: Rock {computer}")
            print("*"*50+"\nIt's a draw\n")
        else:
            print(f"Computer choose: Paper {computer}")
            print("*"*50+"\nYou lose\n")
        
    elif user_choose == 1:
        print(f"You choose: Paper {game[user_choose]}")
        if computer == game[0]:
            print(f"Computer choose: Rock {computer}")
            print("*"*50+"\nYou Win\n")
            exit()
        elif computer == game[2]:
            print(f"Computer choose: Scissor {computer}")
            print("*"*50+"\nYou lose\n")
        else:
            print(f"Computer choose: Paper {computer}")
            print("*"*50+"\nIt's a draw\n")
        
    elif user_choose == 2:
        print(f"You choose: Scissor {game[user_choose]}")
        if computer == game[1]:
            print(f"Computer choose: Paper {computer}")
            print("*"*50+"\nYou Win\n")
            exit()
        elif computer == game[0]:
            print(f"Computer choose: Rock {computer}")
            print("*"*50+"\nYou lose\n")
        else:
            print(f"Computer choose: Scissor {computer}")
            print("*"*50+"\nIt's a draw\n")
    else:
        print("*"*50+"\nInvalid choose.\n")
        exit()