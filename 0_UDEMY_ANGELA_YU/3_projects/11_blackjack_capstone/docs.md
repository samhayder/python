# Blackjack Project

### Chose your difficulty

- Normal: Use all Hints below to complete the project.
- Hard: Use only Hints 1,2,3 to complete the project
- Extra Hard: Only use Hints 1 & 2 to complete the project
- Expert: Only use Hint 1 t0 complete the project

### Our Blackjack Game House Rules

- The deck is unlimited in size.
- There are no jokers.
- The jack/Queen/King all count as 10.
- The Ace can count as 11 or 1.
- cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
- The cards in the list have equal probability fo being drawn.
- Cards are not removed from the dock as they are drawn.
- The computer is the dealer.

### Pseudo

- 1.Create a deal_card() function that users the List below to return a random card.
  - cards = [11,2,3,4,5,6,7,8,9,10,10,10]
  - Remember that 11 is the Ace.
- 2.Deal the user and computer 2 cares each using deal_card() and append().
  - user_cards = []
  - computer_cards = []
- 3.Create a function called a calculate_score() that takes a list of cards as input and returns the sum of all the cards in the list as the score.
- 4.Inside calculate_score() check for a blackjack (a hand with only 2 cards: acc + 10) and return 0 instead of the actual score. 0 will represent a blackjack in our game.
- 5.Inside calculate_score() check for an 11(acc). If the score is already over 21, remove the 11 and replace it with a 1.
- 6.Call the function calculate_score(). If the computer or the user has a blackjack (0) or if the user's score is over 21, then the game ends.
- 7.if the game has not ended, ask the user if they want t draw another card. If yes, then user the deal_card() function to and another card to the user_cards list. If no, then the game has ended.
- 8.The score will need to be rechecked with every new card drawn and the checks in Hint 6 need to be repeated until the game ends.
- 9.Once the user is done, it's time to let the computer play. The computer should keep drawing cards as long as it has a score less than 17.

- 10.Create a function called compare() and pass in the user_score and computer_score.

  - if the computer and user both have the same score, then it's a draw.
  - If the computer has a blackjack(0), then the user loses.
  - If the user has a blackjack (0), then the user wins.
  - If the user_score is over 21, then the user loses.
  - If the computer_score is over 21, then the computer losses.
  - If none of the above, then the player with the highest score wins.

- 11.Ask the user if they want to restart the game. If they answer yes
