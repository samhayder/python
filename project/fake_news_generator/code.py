import random
subjects = ["Salman Khan", "Sakib Al Hasan", "Shek Hasina", "Norendo Modi"]
actions = ["Got Married", "Die", "Detector"]
places = ["Bangladesh","India", "at Mirpur"]


def main():
    while True:
        print("~"*20)
        print("\nWelcome, Fake news headline generator. To continue Yes/No")
        print("~"*20)
        
        user_input = input("Yes or No ").strip().lower()
        if user_input == "no":
            break
        
        
        subject = random.choice(subjects)
        action = random.choice(actions)
        place = random.choice(places)
        print(f"\nBREAKING NEWS: {subject} {action} {place}")
        

if __name__ == '__main__':
    main()