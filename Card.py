class Card(object):

    def __init__(self, rank, suit):

        self.rank = rank
        self.suit = suit

    def setRank(self, rank):

        self.rank = rank

    def setSuit(self, suit):

        self.suit = suit

    def getRank(self):

        return self.rank

    def getSuit(self):

        return self.suit