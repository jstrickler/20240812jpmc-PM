class Card:  # inheriting from 'object'
    def __init__(self, rank, suit):  # this.a = a
        # self.a = a
        self.rank = rank    # store in private instance variable
        self.suit = suit

    def get_rank(self):  # getter METHOD
        return self._rank
    
    @property
    def rank(self):   # getter PROPERTY
        return self._rank

    @rank.setter
    def rank(self, value):   # setter property
        self._rank = value

    @property
    def suit(self):
        return self._suit
    
    @suit.setter
    def suit(self, value):
        if value in ['Clubs', 'Diamonds', 'Hearts', 'Spades', 'Joker']:
            self._suit = value
        else:
            raise ValueError(f"{value} is not a valid suit")

    def __str__(self):  #  str(obj)
        return f"{self.rank}-{self.suit}"

    def __repr__(self):   # repr(obj)
        return f"Card('{self.rank}', '{self.suit}')"

if __name__ == "__main__":
    c1 = Card("10", "Diamonds")
    print(c1)  #   print(str(c1))   human-friendly info
    print(f"{c1 = }")   # repr(c1)  how to reproduce object
    
    print(f"{c1.get_rank() = }")
    print(f"{c1.rank = }")
#    print(f"{c1.get_rank = }")
    print(f"{c1.suit = }")
    c1.rank = "Q"
    print(f"{c1.rank = }")
    # c1.suit = "Wombats"
    # c2 = Card("9", "Wombats")
    
