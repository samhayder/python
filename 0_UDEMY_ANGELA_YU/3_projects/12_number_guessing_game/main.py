from random import randint

# check difficulty
def set_difficulty():
    attempts = 0
    level = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    
    if level == 'easy':
        attempts += 10
    elif level == 'hard':
        attempts += 5
    else:
        print("Invalid.")
        exit()
    return attempts

# check answer to correct condition
def check_answer(user_guess,actual_number,attempt):
    if user_guess > actual_number:
        attempt -= 1
        print("Too High")
    elif user_guess == actual_number:
        attempt -= 1
        print("You win")
        exit()
    else:
        attempt -= 1
        print("Too Low")
    return attempt

# set random number 1 to 100
random_number = randint(1,100)
attempt = set_difficulty()
guess = 0

while guess != random_number:
    print(f"you have {attempt} attempts remaining to guess the number.")
    
    guess = int(input("Make a guess: "))
    
    attempt = check_answer(user_guess=guess,actual_number=random_number,attempt=attempt)
    
    if attempt == 0:
        print("You've run out of guesses, you lose.")
        exit()
    


