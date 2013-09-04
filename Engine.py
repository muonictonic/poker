from Deck import *
from Hand import *

class Engine(object):
    
    #Creates a dictionary to map each type of hand to a corresponding score
	hand_values = {
	    'Pair' : 1, 'Two Pair' : 2, 'Three of a Kind' : 3,
            'Straight' : 4, 'Flush' : 5, 'Full House' : 6,
            'Four of a Kind' : 7, 'Straight Flush' : 8,
            'Royal Flush' : 9, 'High Card' : 0 }
	
    #Builds the deck and adds each player's hand to a list
	def __init__(self, comp_players):
		

		self.comp_players = comp_players

        #Create a list of Hand objects, one for each player
		self.hands = []

		print "Computer Players: ", self.comp_players
		
        #Build and shuffle the deck
		self.poker_deck = Deck()
		self.poker_deck.shuffle()
		
        #Add the player's Hand to self.hands
		self.hands.append(Hand(self.poker_deck.dealHand()))
		
        #Add one Hand to self.hands for each computer player
		for i in range(comp_players):
			self.hands.append(Hand(self.poker_deck.dealHand()))
	
    #Plays the game by comparing the scores of each player's type of hand
	def play(self):
		    
        #Remove the player's hand from self.hands and determines its score
		player_hand = self.hands.pop(0)
		player_score = Engine.hand_values[player_hand.determineScore()]
		
        #Print out the user's hand and its type
		print "*" * 20
		print "     YOUR HAND     "
		print "*" * 20
		player_hand.__str__()		
		print "*" * 20
		print "HAND: ", player_hand.determineScore()
		print "*" * 20
		
		comp_scores = []
		
        #Add each computer player's score to a list
		for i in range(self.comp_players):
			comp_scores.append(Engine.hand_values[self.hands.pop().determineScore()])
		
        #If any computer player has a better hand, the user loses
        #If the player ties for the best hand, the player ties
        #If the player has the highest scoring hand, the user wins
		canWin = True
		for score in comp_scores:
			if player_score < score:
				return 'You lose!'
			elif player_score == score:
				canWin = False
		
		if canWin:
			return 'You win!'
		else:
			return 'You tied!'
			
