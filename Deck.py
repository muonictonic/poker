from Card import *
from random import shuffle

class Deck(object):
 
    ranks = ['Ace', 'Deuce', 'Three', 'Four',
             'Five', 'Six', 'Seven', 'Eight',
	     'Nine', 'Ten', 'Jack', 'Queen', 'King']
        
    suits = ['Hearts', 'Diamonds', 'Spades', 'Clubs']

    def __init__(self):
   
        self.deck = []

        for i in range(52):
            card = Card(Deck.ranks[i % 13], Deck.suits[i / 13])
            self.deck.append(card)

    def shuffle(self):

        return shuffle(self.deck)

    def __str__(self):
	
	i = 0
        for card in self.deck:
	    
	    i += 1
            print "%d - %s of %s" %(
                    i, card.getRank(), card.getSuit())
    
    def dealHand(self):

        hand = []

        for i in range(5):
            hand.append(self.deck.pop())
   
        return hand