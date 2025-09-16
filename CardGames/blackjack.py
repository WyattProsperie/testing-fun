import deck
from deck import *
deck_actions = deck.Deck()
deck = deck_actions.deck

player_hand = []
split_hand1 = []
split_hand2 = []
dealer_hand = []
discard     = []

def calculate_hand_value(hand):
    value = 0
    aces = 0
    
    for card in hand:
        rank = check_rank(card)
        if rank in ["T", "J", "Q", "K"]:
            value += 10
        elif rank == "A":
            aces += 1
            value += 11
        else:
            value += int(rank)
    
    while value > 21 and aces:
        value -= 10
        aces -= 1
    
    return value

money = float(input("Enter the amount of money you have to play with: $"))
round_done = False

i = 51
while i > 0 and money > 0:
    
    if len(player_hand) == 0 and len(dealer_hand) == 0:
        print(f"You have ${money}")
        bet = float(input("Enter your bet amount: $"))

    if len(player_hand) < 2:
        split_game = False
        
        move_piles(deck, i, player_hand)
        i -= 1
        move_piles(deck, i, dealer_hand)
        i -= 1
        move_piles(deck, i, player_hand)
        i -= 1
        move_piles(deck, i, dealer_hand)
        i -= 1
        print(f"Your hand: ", end="")
            
        reveal_cards(player_hand)
        print(f"Dealer's hand: {show_card(flip_card(dealer_hand[0]))} XX")
        
        if check_rank(player_hand[0]) == check_rank(player_hand[1]) and money >= bet * 2 and split_game == False:
            split = input("You have a pair! Type 'S' to split or any other key to continue: ").upper()
            if split == "S":
                
                split_game = True
                
                move_piles(player_hand, 0, split_hand1)
                move_piles(player_hand, 0, split_hand2)
                
                print("Your first split hand: ", end="")
                reveal_cards(split_hand1)
                print("Your second split hand: ", end="")
                reveal_cards(split_hand2)
                
        continue
    
    player_value = calculate_hand_value(player_hand)
    dealer_value = calculate_hand_value(dealer_hand)
    
    if player_value > 21:
        print("Bust! You lose.")
        action = "S"
    elif player_value == 21:
        print("You hit 21! Now it's the dealer's turn.")
        action = "S"
    
    if player_value < 21 and split_game == False:
        action = input("Type 'H' to hit, 'S' to stand: ").upper()
    elif player_value < 21 and split_game == True:
        split_hand = 1
        if split_hand == 1:
            action = input("First split hand. Type 'H' to hit, 'S' to stand: ").upper()
        elif split_hand == 2:
            action = input("Second split hand. Type 'H' to hit, 'S' to stand: ").upper()
        
    if action == "H" and split_game == False:
        move_piles(deck, i, player_hand)
        i -= 1
        print(f"Your hand: ", end="")
        reveal_cards(player_hand)
    elif action == "H" and split_game == True:
        if split_hand == 1:
            move_piles(deck, i, split_hand1)
            i -= 1
            print(f"Your first split hand: ", end="")
            reveal_cards(split_hand1)
        elif split_hand == 2:
            move_piles(deck, i, split_hand2)
            i -= 1
            print(f"Your second split hand: ", end="")
            reveal_cards(split_hand2)
    elif action == "S" and split_game == True:
        if split_hand == 1:
            split_hand = 2
            print("Now playing second split hand.")
            print(f"Your second split hand: ", end="")
            reveal_cards(split_hand2)
            continue
        elif split_hand == 2:
            while dealer_value < 17:
                move_piles(deck, i, dealer_hand)
                i -= 1
                dealer_value = calculate_hand_value(dealer_hand)
            
            print(f"Dealer's hand: ", end="")
            reveal_cards(dealer_hand)
            
            if dealer_value > 21:
                print("Dealer busts! You win both hands!")
                money += bet * 2
            else:
                split1_value = calculate_hand_value(split_hand1)
                split2_value = calculate_hand_value(split_hand2)
                
                if dealer_value == split1_value:
                    print("First split hand is a tie!")
                elif dealer_value > split1_value:
                    print("Dealer wins first split hand!")
                    money -= bet
                else:
                    print("You win first split hand!")
                    money += bet
                
                if dealer_value == split2_value:
                    print("Second split hand is a tie!")
                elif dealer_value > split2_value:
                    print("Dealer wins second split hand!")
                    money -= bet
                else:
                    print("You win second split hand!")
                    money += bet
            round_done = True
    elif action == "S" and split_game == False:
        while dealer_value < 17:
            move_piles(deck, i, dealer_hand)
            i -= 1
            dealer_value = calculate_hand_value(dealer_hand)
        
        print(f"Dealer's hand: ", end="")
        reveal_cards(dealer_hand)
        
        if dealer_value > 21:
            print("Dealer busts! You win!")
            money += bet
        elif dealer_value == player_value:
            print("It's a tie!")
        elif dealer_value > player_value:
            print("Dealer wins!")
            money -= bet
        elif player_value > 21:
            print("You lose.")
            money -= bet
        else:
            print("You win!")
            money += bet
        round_done = True
    else:
        print("Invalid input, please try again.")
        continue
    if round_done:
        round_done = False
        split_game = False
        quit = input("Quit or play again? (Q/P): ").upper()
        if quit == "Q":
            print("Thanks for playing!")
            print(f"You leave with ${money}")
            break
        
        print("--- New Round ---")
        
        while len(player_hand) > 0:
            move_piles(player_hand, 0, discard)
        
        while len(split_hand1) > 0:
            move_piles(split_hand1, 0, discard)
        
        while len(split_hand2) > 0:
            move_piles(split_hand2, 0, discard)
            
        while len(dealer_hand) > 0:
            move_piles(dealer_hand, 0, discard)
    
    if calculate_hand_value(deck) < 42:
        print("Resuffling the deck...")
        
        while len(discard) > 0:
            move_piles(discard, 0, deck)
    
    shuffle_deck(deck)
    
print(f"Game over, you have {money}")