import random

easy = ["God","Bad","Sir","Buy"]
hard = ["Compare","Attempt","Program","Guessed"]

attempt_count = 0

def easy_level(guess_word):
    global attempt_count
    random_easy_word = random.choice(easy).lower()
    print("ransom_easy",random_easy_word)
    
    if guess_word == random_easy_word:
        attempt_count += 1
        print(f"Congratulation! {attempt_count} -attempts to you win.")
        return
    else:
        attempt_count = attempt_count + 1
        print("attempt_count",attempt_count)

def hard_level(guess_word):
    global attempt_count
    random_hard_word = random.choice(hard).lower()
    print("ransom_hard",random_hard_word)
    
    if guess_word == random_hard_word:
        attempt_count += 1
        print(f"Congratulation! {attempt_count} -attempts to you win.")
        return
    else:
        attempt_count = attempt_count + 1
        print("attempt_count",attempt_count)

def main():
    print("Welcome. Password guessing game.\n"+"*" * 50)
    
    level = input("Choose level: easy, hard. ").strip().lower()
    
    while True:
        
        guess_word = input(f"Guess your {level} word to continue game or exit. ").strip().lower()
        
        if guess_word == "exit":
            print("Goodby. Close your password guessing game.\n")
            return
        
        if level == "easy":
            easy_level(guess_word)
        elif level == "hard":
            hard_level(guess_word)
        else:
            print("Invalid choose. Please try again. Only choose:- 'easy' or 'hard'")
            return
        
            

    
if __name__ == "__main__":
    main()