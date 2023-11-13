import random

class Deck:
    def __init__(self):
        self.suits = ['Spades', 'Diamonds', 'Hearts', 'Clubs']
        self.ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
        self.cards = [f'{suit}:{rank}' for suit in self.suits for rank in self.ranks]
        self.shuffle()
              
    def shuffle(self): #shuffle 함수를 이용해 리스트의 카드를 섞는 함수
        random.shuffle(self.cards) # 섞은 후 다시 card에 재배열

    def distributing(self, num_cards): # card를 num_cards만큼 분배
        return [self.cards.pop() for i in range(num_cards)]