import random
deck = []
i = 0

#Hidden, Color, Suit, Rank
cardinfo = "HCSN"
blackcounter = 0
redcounter = 0

spadecounter    = 0
clubcounter     = 0
heartcounter    = 0
diamondcounter  = 0

spaderank      = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K"]
clubrank       = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K"]
heartrank      = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K"]
diamondrank    = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K"]

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
        
    deck.append(thisCardinfo)
    i += 1
    
print(deck)
print(i)
print(f"Black: {blackcounter}, Red: {redcounter}")
print(f"Spades: {spadecounter}, Clubs: {clubcounter}, Hearts: {heartcounter}, Diamonds: {diamondcounter}")