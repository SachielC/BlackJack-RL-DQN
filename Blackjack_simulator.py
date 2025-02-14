import random
import numpy as np
def draw():
    cards = [2,3,4,5,6,7,8,9,10,10,10,10,11]
    return random.choice(cards)

def deal():
    hand = [draw(), draw()]
    return sum(hand), hand
def Naive_blackjack():
    ##starting hand
    aces = 0
    total = random.randint(2,11)
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
        return 'Bust'
    return total 


def simulate_blackjack(n):
    results = {}
    for i in range(n):
        play = (Naive_blackjack())
        if play in results:
            results[play] += 1
        else:
            results[play] = 1
    return (results)

simulate_blackjack(100000)

