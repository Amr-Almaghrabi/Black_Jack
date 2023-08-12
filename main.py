############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

#------------------------------------------------------------------
import random
from art import logo
import replit



def black_jack():
  print(logo)
  print(f"Welcome to black jack ! \n")
  cards =[11,2,3,4,5,6,7,8,9,10,10,10,10]
  
  user_hand=[]
  user_total = 0
  for i in range(2):
    new_card = random.choice(cards)
    user_hand.append(new_card)
    user_total += new_card

  
  

  
  print(f"Your current hand cards are: {user_hand} totaling {user_total}")
  
  computer_hand =[]
  
  computer_hand.append(random.choice(cards))
  
  print(f"The computer's hand is {computer_hand}")
  
  
  
  more_cards = input("Would you like to draw another card ? (type y/n) ")
  checker = True
  while checker:
    while more_cards == 'y':
      new_card = random.choice(cards)
      user_hand.append(new_card)
      user_total += new_card
      print(f"your cards are {user_hand}, total is {user_total}")
      more_cards = input("Would you like to draw another card ? (type y/n) ")

    if user_total >21 and 11 in user_hand:
      user_hand.remove(11)
      user_hand.append(1)

    if sum(user_hand) == 21 and len(user_hand) == 2:
      print(f"You have blackjack , your cards are {user_hand} totaling 0")
      return 0
    
    

    user_total = sum(user_hand)
    
    new_card = random.choice(cards)
    computer_hand.append(new_card)
    computer_total = sum(computer_hand)

    if computer_total >21 and 11 in computer_hand:
      computer_hand.remove(11)
      computer_hand.append(1)

    computer_total = sum(computer_hand)
    print(f"Your hand is {user_hand}")
    print(f"Computer hand is {computer_hand}")

    
    if user_total > 21:
      print( 'You have a bust, you lose :(') 
  
    elif computer_total >21:
      print(f"Computer has a bust, you win!")
    
    elif user_total == computer_total:
      print(f"it's a draw")
  
    elif user_total > computer_total:
      print(f"Your total is {user_total} and computer total is {computer_total}, you win !")
  
    else:
      print(f"Your total is {user_total}, computer total is {computer_total} computer wins :( ")
  
    play_again = input("Would you like to play again? (yes/no) ")
    play_again = play_again.lower()
    
    if play_again == 'yes':
      replit.clear()
      black_jack()
    else:
      checker = False
      return

  return


black_jack()


  

  
