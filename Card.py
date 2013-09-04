class Card(object):

    def __init__(self, rank, suit):

        self.rank = rank
        self.suit = suit
    
    #Set functions for rank and suit
    def setRank(self, rank):

        self.rank = rank

    def setSuit(self, suit):

        self.suit = suit
    
    #Get functions for rank and suit
    def getRank(self):

        return self.rank

    def getSuit(self):

        return self.suit
