# Number Guessing Game

### Pseudocode
- print("welcome to the Number Guessing Game?")
- print("I'm thinking of a number between 1 and 100.")
- input("Choose a difficulty. Type 'easy' or 'hard': ).lower()
- if-> 'easy'== print("you have 10 attempts remaining to guess the number. )
- if-> 'hard'== print("you have 10 attempts remaining to guess the number. )
- int(input("Make a guess: "))
- if guess > number-> print("Too high.")
- print("Guess again.")
- print("You have 4 attempts remaining to guess the number.")
- int(input("Make a guess: ))
- if guess < number-> print("Too low.")
- when attempts is null print("You've run out of guesses, you lose.)