
from random import shuffle



class Card:
    def __init__(self,type,value):
        self.type = type
        self.value = value

    def __repr__(self):
        return f"{self.type} , {self.value}"




class Deck:
    types = ["karo", "sinek", "kupa", "maça"]
    values = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]


    def __init__(self):
        self.cards = [Card(type,value) for type in Deck.types for value in Deck.values]
        print(self.cards)


    def countofcards(self):
        return len(self.cards)


    def mixCards(self):
        if (self.countofcards()<52):
            raise ValueError("you cannot mix the cards.")
        shuffle(self.cards)


    def dealCards(self,number):
        countofcards = self.countofcards()
        if countofcards ==0:
            raise ValueError("all cards dealt.")
        number = min(countofcards,number)
        cards = self.cards[-number:]
        self.cards = self.cards[:-number]
        return cards


    def throwCard(self):
        return self.dealCards(1)[0]

deck = Deck()
deck.mixCards()


print(f"discarded card : {deck.throwCard()}")
print(f"your cars are : {deck.dealCards(7)}")
print(f"count of cards are :{deck.countofcards()}")
print(f"remaining card : {deck.cards}")