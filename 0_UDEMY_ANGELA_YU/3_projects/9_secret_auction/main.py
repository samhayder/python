print("*** Welcome to The Secret Auction Program ***")

bidder_details = {}

should_continue = True

def find_highest_bidder(bidder_dictionary):
    winner = ""
    highest_bidder = 0
    
    for bidder in bidder_dictionary:
        bid_amount = bidder_dictionary[bidder]
        
        if bid_amount > highest_bidder:
            highest_bidder = bid_amount
            winner = bidder
    print("*" * 50)
    print(f"The winner is {winner} with a bid of ${highest_bidder}")
    print("*" * 50)

while should_continue:
    bidder_name = input("What is your name? ").lower()
    bidder_price = float(input("What's your bid? $"))
    
    bidder_details[bidder_name] = bidder_price
    
    add_bidder = input("Are there any other bidders? Type 'yes' or 'no' \n").lower()
    
    if add_bidder == "no":
        find_highest_bidder(bidder_details)
        should_continue = False
