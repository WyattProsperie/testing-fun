import deck
from deck import *

print("Creating a new deck...")
deck_actions = deck.Deck()


deck = deck_actions.deck
discard = []

print(f"Your first card is: {show_card(flip_card(deck[51]))}")
rank_list = ["2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K", "A"]

i = 51
while i > 0:
    options = input("Type 'H' to guess higher, 'L' to guess lower, or 'Q' to quit: ").upper()
    
    if options == "Q":
        print("Thanks for playing!")
        break
    elif options != "H" and options != "L":
        print("Invalid input, please try again.")
        continue
    else:
        print(f"Your current card is: {check_rank(deck[i])} of {check_suit(deck[i])}")
        move_piles(deck, i, discard)
        i -= 1
        print(f"The next card is: {check_rank(deck[i])} of {check_suit(deck[i])}")
        
        if (options == "H"):
            if rank_list.index(check_rank(deck[i])) > rank_list.index(check_rank(discard[-1])):
                print("You guessed correctly!")
        
        elif (options == "L"):
            if rank_list.index(check_rank(deck[i])) < rank_list.index(check_rank(discard[-1])):
                print("You guessed correctly!")
        else:
            print("Sorry, you guessed incorrectly.")
        
        move_piles(deck, i, discard)
        i -= 1
        
        if i < 0:
            print("No more cards left! Thanks for playing!")
            break