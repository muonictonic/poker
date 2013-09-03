from Deck import *
from Hand import *

class Engine(object):

	hand_values = {
	    'Pair' : 1, 'Two Pair' : 2, 'Three of a Kind' : 3,
            'Straight' : 4, 'Flush' : 5, 'Full House' : 6,
            'Four of a Kind' : 7, 'Straight Flush' : 8,
            'Royal Flush' : 9, 'High Card' : 0 }
	    
	def __init__(self, comp_players):
		
		self.comp_players = comp_players
		self.hands = []
		print "Computer Players: ", self.comp_players
		
		self.poker_deck = Deck()
		self.poker_deck.shuffle()
		
		self.hands.append(Hand(self.poker_deck.dealHand()))
		
		for i in range(comp_players):
			self.hands.append(Hand(self.poker_deck.dealHand()))
						
	def play(self):
		
		player_hand = self.hands.pop(0)
		player_score = Engine.hand_values[player_hand.determineScore()]
		
		print "*" * 20
		print "     YOUR HAND     "
		print "*" * 20
		player_hand.__str__()		
		print "*" * 20
		print "HAND: ", player_hand.determineScore()
		print "*" * 20
		
		comp_scores = []
		
		for i in range(self.comp_players):
			comp_scores.append(Engine.hand_values[self.hands.pop().determineScore()])
									
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
			