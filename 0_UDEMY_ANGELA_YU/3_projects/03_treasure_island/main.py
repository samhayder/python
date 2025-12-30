print(r'''
                    ____...------------...____
               _.-"` /o/__ ____ __ __  __ \o\_`"-._
             .'     / /                    \ \     '.
             |=====/o/======================\o\=====|
             |____/_/________..____..________\_\____|
             /   _/ \_     <_o#\__/#o_>     _/ \_   \
             \_________\####/_________/
              |===\!/========================\!/===|
              |   |=|          .---.         |=|   |
              |===|o|=========/     \========|o|===|
              |   | |         \() ()/        | |   |
              |===|o|======{'-.) A (.-'}=====|o|===|
              | __/ \__     '-.\uuu/.-'    __/ \__ |
              |==== .'.'^'.'.====|
          jgs |  _\o/   __  {.' __  '.} _   _\o/  _|
              `""""-""""""""""""""""""""""""""-""""`
''')

print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
choice_1 = input('You\'r at a crossroad, Where do yu want to go? Type "Left" or "Right"\n').strip().lower()

if choice_1 == "left":
    choice_2 = input('you\'ve come to a Lake, there is a island in the middle of the lake. Type "Wait" to wait for a boat. Type "Swim" to swim crosse\n').strip().lower()
    
    if choice_2 == "wait":
        choice_3 = input('You arrive at he island unharmed. There is house with 3 doors. One "Red", one "Yellow" and one "Blue". Which color do you choose.\n').strip().lower()
        
        if choice_3 == "red":
            print("Game Over! Burned by fire.")
            exit()
        elif choice_3 == "yellow":
            print("Congratulation! You Win.")
            exit()
        elif choice_3 == "blue":
            print("Game Over! Eaten by beasts.")
            exit()
        else:
            print("Game Over! Wrong choose door.")
            exit()
    else:
        print("Game Over! Fall into a hole")
        exit()
else:
    print("Game Over! Choose the wrong way.")
    exit()