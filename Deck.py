from Card import *
from random import shuffle

class Deck(object):
    
    #Set the possible ranks and suits
    ranks = ['Ace', 'Deuce', 'Three', 'Four',
             'Five', 'Six', 'Seven', 'Eight',
	     'Nine', 'Ten', 'Jack', 'Queen', 'King']
        
    suits = ['Hearts', 'Diamonds', 'Spades', 'Clubs']

    #Create a list of 52 Card objects of each rank for each suit
    def __init__(self):
        
        self.deck = []

        for i in range(52):
            card = Card(Deck.ranks[i % 13], Deck.suits[i / 13])
            self.deck.append(card)

    def shuffle(self):

        return shuffle(self.deck)

    #Prints the cards as '<rank> of <suit>'
    def __str__(self):
	
        i = 0
        for card in self.deck:
	    
	    i += 1
            print "%d - %s of %s" %(
                    i, card.getRank(), card.getSuit())
    
    #Creates a list of 5 Card objects by removing them from self.deck
    def dealHand(self):

        hand = []

        for i in range(5):
            hand.append(self.deck.pop())
   
        return hand
