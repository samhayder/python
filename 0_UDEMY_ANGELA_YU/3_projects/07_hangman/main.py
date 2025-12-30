import random
from hangman_art import stages,logo

words = ['act','action','activity','actually','add','address','administration','beat','beautiful','because','become','bed','before','begin','behavior','century','certain','certainly','chair','challenge','chance','change']

random_word = random.choice(words).lower()
placeholder = ""
result = []
lives = 6
game_over = False

print(logo)

for i in range(len(random_word)):
    placeholder += "-"
print(f"Word to guess {placeholder}")   

while not game_over:
    display = ""
    guess_char = input("\nGuess a character. ").strip().lower()
    
    if guess_char == "exit":
        print("Goodby! The game is close.")
        game_over = True
        exit()
    
    for char in random_word:
        if char == guess_char:
            display += char
            result.append(char)
        elif char in result:
            display += char
        else:
            display += "-"
            
    print(f"Word to guess {display}")
    
    if guess_char not in random_word:
        lives -= 1
        print(f"Your guessed {guess_char}, that's not in the word. you lose a life")
        print(stages[lives])
        print(f"{'*'*10} {lives}/6 LIVES LEFT {'*'*10}")
    
    if "-" not in display:
        print(f"{'*'*50} \nYou Win\n {'*'*50}")
        game_over = True
    
    if lives == 0:
        print(f"{'*'*50} \nYou Lose\n {'*'*50}")
        game_over = True
    
    
    
    
    
    