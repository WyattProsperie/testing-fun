import random

class Deck :
    def __init__(self):
        self.deck = []
    
        i = 0

        #Hidden, Color, Suit, Rank
        cardinfo    = "ZCSN"
        ranks_short = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K"]

        blackcounter    = 0
        redcounter      = 0
        spadecounter    = 0
        clubcounter     = 0
        heartcounter    = 0
        diamondcounter  = 0

        spaderank      = ranks_short.copy()
        clubrank       = ranks_short.copy()
        heartrank      = ranks_short.copy()
        diamondrank    = ranks_short.copy()

        while i < 52:
            
            # thisCardinfo = cardinfo.replace("H", "0")
            
            color = random.randint(0,1)
            
            if color == 1 and redcounter == 26:
                color = 0
            elif color == 0 and blackcounter == 26:
                color = 1
                
            if color == 0 and blackcounter < 26:
                thisCardinfo = cardinfo.replace("C", "B")
                blackcounter += 1
            else: # if color == 1 and redcounter < 26:
                thisCardinfo = cardinfo.replace("C", "R")
                redcounter += 1
                
            suit = random.randint(0,1)
            
            if color == 0:
                
                if suit == 0 and spadecounter == 13:
                    suit = 1
                elif suit == 1 and clubcounter == 13:
                    suit = 0  
                    
                if suit == 0 and spadecounter < 13:
                    spadecounter += 1
                else: # if suit == 1 and clubcounter < 13:
                    thisCardinfo = thisCardinfo.replace("S", "C")
                    clubcounter += 1
                    
            else:
                
                if suit == 0 and heartcounter == 13:
                    suit = 1
                elif suit == 1 and diamondcounter == 13:
                    suit = 0
                    
                if suit == 0 and heartcounter < 13:
                    thisCardinfo = thisCardinfo.replace("S", "H")
                    heartcounter += 1
                else: # if suit == 1 and diamondcounter < 13:
                    thisCardinfo = thisCardinfo.replace("S", "D")
                    diamondcounter += 1
                    
            if thisCardinfo[2] == "S":
                rank = random.choice(spaderank)
                thisCardinfo = thisCardinfo.replace("N", rank)
                spaderank.remove(rank)
            elif thisCardinfo[2] == "C":
                rank = random.choice(clubrank)
                thisCardinfo = thisCardinfo.replace("N", rank)
                clubrank.remove(rank)
            elif thisCardinfo[2] == "H":
                rank = random.choice(heartrank)
                thisCardinfo = thisCardinfo.replace("N", rank)
                heartrank.remove(rank) 
            elif thisCardinfo[2] == "D":
                rank = random.choice(diamondrank)
                thisCardinfo = thisCardinfo.replace("N", rank)
                diamondrank.remove(rank)
            
            self.deck.append(thisCardinfo)
            i += 1

def from_deck(list, int, list2):
    card = list.pop(int)
    list2.append(card)
    return

def move_piles(list, int, list2):
    card = list.pop(int)
    list2.append(card)
    return

def flip_card(card):
    if card[0] == "Z":
        card = card.replace("Z", "V")
    else:
        card = card.replace("V", "Z")
    return card

def show_cards(list):
    for card in list:
        if card[0] == "Z":
            print("XX", end=" ")
        else:
            suit = check_suit(card)
                
            if suit == "S":
                print(f"♠{check_rank(card)}", end=" ")
            elif suit == "C":
                print(f"♣{check_rank(card)}", end=" ")
            elif suit == "H":
                print(f"♥{check_rank(card)}", end=" ")
            elif suit == "D":
                print(f"♦{check_rank(card)}", end=" ")           
    print()
    return

def reveal_cards(list):
    
    for card in list:
        suit = check_suit(card)
                
        if suit == "S":
            print(f"♠{check_rank(card)}", end=" ")
        elif suit == "C":
            print(f"♣{check_rank(card)}", end=" ")
        elif suit == "H":
            print(f"♥{check_rank(card)}", end=" ")
        elif suit == "D":
            print(f"♦{check_rank(card)}", end=" ")           
    print()
    return

def show_card(card):
    if card[0] == "Z":
        return "XX"
    else:
        suit = check_suit(card)
            
        if suit == "S":
            return f"♠{check_rank(card)}"
        elif suit == "C":
            return f"♣{check_rank(card)}"
        elif suit == "H":
            return f"♥{check_rank(card)}"
        elif suit == "D":
            return f"♦{check_rank(card)}"           
    return

def shuffle_deck(list):
    random.shuffle(list)
    return
    
def check_suit(card):
    return card[2]

def check_rank(card):
    return card[3]

def check_color(card):
    return card[1]