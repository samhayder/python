import random

easy_words = ["apple", "train", "tiger", "money", "india"]
medium_words = ["python", "bottle", "monkey", "planet", "laptop"]
hard_words = ["elephant", "diamond", "umbrella", "computer", "mountain"]

print("Welcome password guessing game.")
level = input("Choose level- easy, medium, hard ").strip().lower()

if level == "easy":
    secret = random.choice(easy_words)
elif level == "medium":
    secret = random.choice(medium_words)
elif level == "hard":
    secret = random.choice(hard_words)
else:
    print("Don't the match level. Try again, or auto selected easy level")
    secret = random.choice(easy_words)

attempts = 0

while True:
    guess = input("Guess secret password. ").strip().lower()
    attempts += 1
    hint = ""
    
    if secret == guess:
        print(f"Congratulation! Your guessed it in {attempts} attempts.")
        break
    for i in range(len(secret)):
        if i < len(guess) and secret[i] == guess[i]:
            hint += guess[i]
        else:
            hint += "_"
    print(f"*****Hint- {hint}")
print("\nGame over.**********")