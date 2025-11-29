# Password Guessing Game

### 1. What are we building?

A simple text-based game where:

- The computer picks a secret password (word).
- The user keeps guessing the word.
- After each guess, the program gives a hint about how close the guessing was (e.g., how many letters are correct and in the correct place).
- The game counts how many guesses it took.
- You can add different difficulty levels (shorter or longer password).

### 2. How does if work?

Step-by-step

  1. The program chooses a secret word (e.g., "banana").
  2. The user is told how many letters the word has.
  3. The program asks the user to guess the word.
  4. After each guess:
    - If correct, the user wins and the program shows the number of attempts.
    - If not, the program gives a hint (e.g., "2 letters are correct and in the right place").
  5. The game continues until the user guesses correctly.

- Bonus: Let the user choose a difficulty:
  1. Easy: 3-letter words
  2. Difficult: 6-letter words

### 3. Concept

|Concept|How it's used|
|----|----|
Loops|Keep asking until correct guess|
Strings|Comparing user input to password|
Conditionals|check if guess is correct, give hints|
Variables|Count attempts, store guesses|
Lists|For word banks, if you wand random words|

### 4. Pseudocode

> 1. START the program
> 2. SHOW welcome message and rules
> 3. LET user choose a difficulty level
>   a. Based on level, set a list of possible secret words
> 4. RANDOMLY select a secret word from the chosen list
> 5. TELL the user how many letters are in the secret word
> 6. SET attempt counter to 0
> 7. WHILE the user hasn't guessed the word:
>   a. ASK user to enter a guess
>   b. INCREMENT attempt counter
>   c. If Guess equal secret word:
>     i. PRINT "Congratulations!" and show attempts
>     ii. BREAK loop
>   d. ELSE:
>     i. COMPARE each letter in the guess to the secret word
>     ii. COUNT how many letters are correct and in the correct place
>
