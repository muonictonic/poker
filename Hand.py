from Deck import *

class Hand(object):

    def __init__(self, hand):

        self.hand = hand
        self.sortHand()
     
    #Sorts the hand by rank and suit
    def sortHand(self):

        self.hand.sort()

    #Creates a histogram of the frequencies of each rank for use
    #in determining the hand's type
    def rankHistogram(self):

        h = dict()
        
        for card in self.hand:

            if card.rank not in h:
                h[card.rank] = 1
            else:
                h[card.rank] += 1
        
        return h
    
    #Returns a list of the ranks of each card in the hand
    def getRankList(self):
        
        ranks = []

        for card in self.hand:
            ranks.append(card.rank)

        return ranks

    #Returns a list of the suits of each card in the hand
    def getSuitList(self):

        suits = []

        for card in self.hand:
            suits.append(card.suit)

        return suits
    
    #Returns true if there is a pair in the hand, and the value of those cards
    def pair(self):
        
        onePair = False

        for rank, freq in self.rankHistogram().items():
            if freq == 2:
                return True, rank

        return False, None
    
    #Returns true if there are twp pairs in the hand, 
    #and the value of those cards
    def twoPair(self):
        
        havePair = False

        for rank, freq in self.rankHistogram().items():
            if freq == 2 and not havePair:
                rank1 = rank
                havePair = True
            elif freq == 2 and havePair:
                return True, rank1, rank

        return False, None, None
    
    #Returns true if there is a three of a kind in the hand,
    #and the value of those cards
    def threeOfaKind(self):

        for rank, freq in self.rankHistogram().items():
            if freq == 3:
                return True, rank
            
        return False, None
    
    #Returns true if there is a four of a kind in the hand,
    #and the value of those cards
    def fourOfaKind(self):
       
        for rank, freq in self.rankHistogram().items():
            if freq == 4:
                return True, rank

        return False, None  
    
    #Returns true of the hand is a straight
    def straight(self):
 
        ranks = self.sortRank(self.getRankList())

        for i in range(len(ranks) - 1):
            if ranks[i + 1] != ranks[i] + 1:
                return False

        return True  
    
    #Returns true is the hand is a straight flush
    def straightFlush(self):

        if not self.straight():
            return False

        for i in range(len(self.hand) - 1):
            if self.hand[i].suit != self.hand[i].suit:
                return False
        
        return True 
    
    #Returns true if the hand is a full house, 
    #and the value of the high card
    def fullHouse(self):

        pair, temp1   = self.pair()
        triple, temp2 = self.threeOfaKind()

        if not (triple and pair):
            return False, None, None
        
        high, low, = None, None
               
        for rank, freq in self.rankHistogram().items():
            if freq == 3:
                high = rank
            else: 
                low = rank
        return True, high, low

    #Returns true if the hand is a flush
    def flush(self):

        suits = self.getSuitList()

        for i in range(len(suits) - 1):
            if self.hand[i + 1].suit != self.hand[i].suit:
                return False
        
        return True
    
    #Returns true if the hand is a Royal Flush
    def royalFlush(self):

        if not self.flush():
            return False

        royals = ['Ten','Jack', 'Queen', 'King', 'Ace']
        ranks = self.getRankList()
       
        i = 0
        for rank in ranks:
            if rank in royals:
                i += 1
                
        if i == 5:
            return True

        return False
    
    #Returns a list of numbers that correspond
    #to the ranks of each card in the hand
    def sortRank(self, ranks):

        ref = dict()
        i = 1

        for rank in Deck.ranks:
            ref[rank] = i
            i += 1
        
        num_hand = []
        for card in self.hand:
            num_hand.append(ref[card.rank])
        
        return num_hand

    
    #Prints the values of each card in the hand,
    #as <rank> of <suit>
    def __str__(self):
        
        for card in self.hand:
            print "%s of %s" % (
                  card.getRank(), card.getSuit())
	
    #Determines which is the best possible type of the hand.
    #And returns the name of the hand to be used in the dictionary
    #in the Engine class
    def determineScore(self):
	
        pair, high = self.pair()
        if pair:
            return 'Pair'
	    
        twoPair, high, low = self.twoPair()
        if twoPair:
            return 'Two Pair'
	    
        triple, high = self.threeOfaKind()
        if triple:
            return 'Three of a Kind'
	    
        if self.straight():
            return 'Straight'
	    
        if self.flush():
            return 'Flush'
	    
        full, high, low = self.fullHouse()
        if full:
            return 'Full House'
	    
        quad, high = self.fourOfaKind()
        if quad:
            return 'Four of a Kind'
	    
        if self.straightFlush():
            return 'Straight Flush'
	    
        if self.royalFlush():
            return 'Royal Flush'
	    
	else:
	    return 'High Card'
