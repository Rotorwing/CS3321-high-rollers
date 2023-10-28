import card

"""Luna Steed
High Rollers CardDeck Class
This class stores an array of 52 cards, with all suits and values."""
class CardDeck:
    def __init__ (self):
        startcard = card.Card(1, "Clubs")
        self.deckarr = [startcard]

    def deckgen(self):
        for x in range(13):
            for y in range(4):
                if y == 0:
                    newcard = card.Card(x, "Clubs")
                    self.deckarr.append(newcard)
                elif y == 1:
                    newcard = card.Card(x, "Diamonds")
                    self.deckarr.append(newcard)
                elif y == 2:
                    newcard = card.Card(x, "Hearts")
                    self.deckarr.append(newcard)
                elif y == 3:
                    newcard = card.Card(x, "Clubs")
                    self.deckarr.append(newcard)

