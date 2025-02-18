import random
import numpy as np
def draw():
    cards = [2,3,4,5,6,7,8,9,10,10,10,10,11]
    return random.choice(cards)

def deal():
    hand = [draw(), draw()]
    return sum(hand), hand
def Play_blackjack(player_type = 'Player'): #Lazy implementation, probably could be much more consice but the code is functional
    ##starting hand
    if player_type == 'Player':
        aces = 0
        total = draw()
        if total == 11:
            aces = 1
        drawn = draw()
        if drawn == 11:
            aces += 1
        while total < 17:
            total += drawn
            if total > 21 and aces > 0:
                total -= 10
                aces -= 1
            drawn = draw()
            if drawn == 11:
                aces += 1
        if total > 21:
            return 0
        return total 
    
    elif player_type == 'Dealer':
        aces = 0
        hand = deal()
        total = hand[0]
        for item in hand[1]:
            if item == 11:
                aces += 1
        open_card = hand[1][0]
        while total < 17:
            total += drawn
            if total > 21 and aces > 0:
                total -= 10
                aces -= 1
            drawn = draw()
            if drawn == 11:
                aces += 1
        if total > 21:
            return 0
        return total, open_card
    else:
        return("Invalid player type, should be 'Player' or 'Dealer'!")
    
def dealer_from_hand(hand):
        aces = 0
        total = hand
        if hand == 11:
            aces = 1
        while total < 17:
            if total > 21 and aces > 0:
                total -= 10
                aces -= 1
            drawn = draw()
            if drawn == 11:
                aces += 1
            total += drawn
        if total > 21:
            return 0
        return total

def simulate_blackjack(n):
    results = {} 
    for i in range(n):
        play = (Play_blackjack())
        if play in results:
            results[play] += 1
        else:
            results[play] = 1
    return (results)



simulate_blackjack(100000)

