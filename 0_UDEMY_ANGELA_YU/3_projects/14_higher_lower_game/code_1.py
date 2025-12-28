import random
from game_data import data

score = 0
game_continue = True

while game_continue:
    compare_a = random.choice(data)
    compare_b = random.choice(data)
    # it's a == b to generate new data
    if compare_a == compare_b:
        compare_b = random.choice(data)
        
    compare_a_follower = compare_a['follower_count']
    compare_b_follower = compare_b['follower_count']

    print(f"\nCompare A: {compare_a['name']}, {compare_a['description']}, {compare_a['country']}\n")

    print("********** VS *********")

    print(f"\nCompare B: {compare_b['name']}, {compare_b['description']}, {compare_b['country']}\n")

    compare = input("Who has more followers? Type 'A' or 'B': ").lower()

    if compare == 'a':
        if compare_a_follower > compare_b_follower:
            score += 1
            print(f"\nYou're Right. Current score: {score}\n")
        else:
            print(f"\nSorry, that's wrong. Final score: {score}\n")
            game_continue = False
    elif compare == 'b':
        if compare_a_follower < compare_b_follower:
            score += 1
            print(f"\nYou're Right. Current score: {score}\n")
        else:
            print(f"\nSorry, that's wrong. Final score: {score}\n")
            game_continue = False
    else:
        print("Invalid input.")
        exit()
        