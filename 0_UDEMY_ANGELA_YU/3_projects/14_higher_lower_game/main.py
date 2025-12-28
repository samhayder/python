import random
from game_data import data
from art import logo,vs

# Display data
def display_data(data):
    return f"{data['name']}, a {data['description']}, from {data['country']}"

# Check Answer
def compare(user_guess,first_compare,last_compare):
    if first_compare > last_compare:
        return user_guess == 'a'
    else:
        return user_guess == 'b'
    

print(logo)

score = 0
game_should_continue = True
compare_b = random.choice(data)

while game_should_continue:
    compare_a = compare_b
    compare_b = random.choice(data)
    if compare_a == compare_b:
        compare_b = random.choice(data)

    compare_a_follower = compare_a['follower_count']
    compare_b_follower = compare_b['follower_count']

    print("Compare A: ", display_data(compare_a))

    print(vs)

    print("Against B: ", display_data(compare_b))

    guess = input("Who has more followers? Type 'A' or 'B': ").lower()
    
    # Clear The screen
    print("\n" * 20)
    print(logo)

    is_guess = compare(user_guess=guess,first_compare=compare_a_follower,last_compare=compare_b_follower)

    if is_guess:
        score += 1
        print(f"You're Right. Current score: {score}")
    else:
        print(f"Sorry that's wrong. Final score: {score}")
        game_should_continue = False
        
   
