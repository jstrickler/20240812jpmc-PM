import random
from card import Card

class CardDeck:
    RANKS = "2 3 4 5 6 7 8 9 10 J Q K A".split()
    SUITS = "Clubs Diamonds Hearts Spades".split()

    def __init__(self):
        self._make_deck()

    def _make_deck(self):
        self._cards = []
        for suit in self.SUITS:
            for rank in self.RANKS:
                card = Card(rank, suit)
                self._cards.append(card)

    @property
    def cards(self):
        return self._cards

    def shuffle(self):
        random.shuffle(self._cards)

    def draw(self):
        return self._cards.pop()

    def __str__(self):
        my_type = type(self)
        return f"{my_type.__name__}:{len(self)}"

    def __repr__(self):
        my_type = type(self)
        return f"{my_type.__name__}()"

    def __len__(self):
        return len(self._cards)


if __name__ == "__main__":
    cd1 = CardDeck()
    print(f"{cd1 = }")
    cd1.shuffle()
    print(f"{cd1.cards = }")
    print(f"{len(cd1) = }")
    
    for _ in range(5):
        card = cd1.draw()
        print(card, repr(card))
    print(cd1)        
