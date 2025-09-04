import random
deck = []
i = 0

#Hidden, Color, Suit, Rank
cardinfo = "HCSN"
blackcounter = 0
redcounter = 0

while i < 52:
    
    thisCardinfo = cardinfo.replace("H", "0")
    
    color = random.randint(0,1)
    
    if color == 0 and blackcounter < 26:
        thisCardinfo = cardinfo.replace("C", "B")
        blackcounter += 1
    
    elif color == 1 and redcounter < 26:
        thisCardinfo = cardinfo.replace("C", "R")
        redcounter += 1
        
    deck.append(thisCardinfo)
    i += 1
    
print(deck)

#hibabyyyy