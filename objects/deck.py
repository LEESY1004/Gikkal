import random

class Deck:
    def __init__(self):
        self.suits = ['하트', '다이아몬드', '스페이드', '클로버']
        self.ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        self.cards = [f'{suit}:{rank}' for suit in self.suits for rank in self.ranks]
            
    def display_deck(self):
        for card in self.cards:
            print(card)
    
    def shuffle(self):
        random.shuffle(self.cards)

    def distributing(self, num_cards):
        return [self.cards.pop() for i in range(num_cards)]
    
deck = Deck()
deck.shuffle()
