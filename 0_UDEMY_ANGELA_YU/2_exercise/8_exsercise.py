def calculate_love_score(name1,name2):
    both_people = name1.lower() + name2.lower()
    love = 0
    true = 0
    love_occurs = "love"
    true_occurs = "true"
    
    for i in both_people:
        if i in true_occurs:
            true += 1
        
        if i in love_occurs:
            love += 1 
    
    print(f"Love Score = {true}{love}")

calculate_love_score("Angela Yu", "Jack Bauer")
calculate_love_score("Kanye West", "Kim Kardashian")