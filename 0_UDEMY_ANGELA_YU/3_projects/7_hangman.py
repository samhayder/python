#What-> Hangman game basically a random word guessing game. User try 6 time to guess the correct word.
#Pseudocode->
"""
1. create word list
2. get user input - accept lowercase
2. check to word list
"""
import random

guess_words_list = ["Teacher", "Mother", "Bangladesh"]
guess_words_random = random.choice(guess_words_list).lower()
guess_words_random_length = len(guess_words_random)
placeholder = ""
correct_word = []
game_over = False
stages = [
    r"""
          _______
     |/      |
     |      (_)
     |      \|/
     |       |
     |      / \
     |
 ____|___
 ________
    """,
    r"""
          _______
     |/      |
     |      (_)
     |      \|/
     |       |
     |      / 
     |
 ____|___
 ________
    """,
    r"""
          _______
     |/      |
     |      (_)
     |      \|/
     |       |
     |       
     |
 ____|___
 ________
    """,
    r"""
          _______
     |/      |
     |      (_)
     |      \|/
     |       
     |       
     |
 ____|___
 ________
    """,
    r"""
          _______
     |/      |
     |      (_)
     |      
     |       
     |       
     |
 ____|___
 ________
    """,
    r"""
          _______
     |/      |
     |      
     |      
     |       
     |       
     |
 ____|___
 ________
    """
]
lives = 5

for i in guess_words_random:
    placeholder += "-"
print(placeholder)

while not game_over:
    display = ""
    user_guess_char = input("Guess a letter. ").strip().lower()
    if len(user_guess_char) > 2:
        print("Please type a single letter.")
        exit()
        
    for char in guess_words_random:
        if char == user_guess_char:
            display += char
            correct_word.append(char)
        elif char in correct_word:
            display += char
        else:
            display += "-"
        
    if user_guess_char not in guess_words_random:
        lives -= 1
        if lives == 0:
            game_over = True
            print("*"*50)
            print("You lose.")   
    
    if "-" not in display:
        game_over = True
        print("*"*50)
        print("You win.")
    
    print(display)
    print(stages[lives])