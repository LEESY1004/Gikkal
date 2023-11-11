from .deck import Deck
from .batting import Batting

class PlayGame:
    def __init__(self):
        self.player_hand = []
        self.dealer_hand = []
        self.deck = Deck()
        self.batting = Batting()
        self.play_blackjack_set()

    def calculate_hand_value(self, hand):
        self.batting.get_bet_amount()  
        value = 0
        num_aces = 0

        for card in hand:
            rank = card.split(":")[1].strip()  # 카드 문자열에서 숫자 또는 랭크 추출
            if rank.isdigit():
                value += int(rank)
            elif rank in ["K", "Q", "J"]:
                value += 10
            elif rank == "A":
                num_aces += 1
                value += 11  # 일단 11로 더하고 나중에 1로 변경할 수 있음

        # Ace를 1로 변경하여 버스트를 피하려는 로직
        while num_aces > 0 and value > 21:
            value -= 10
            num_aces -= 1

        return value

    def play_blackjack_set(self):
        deck = Deck()
        deck.shuffle()

        # 플레이어와 딜러에게 각각 2장의 카드를 나눠줌
        self.player_hand = deck.distributing(2)
        self.dealer_hand = deck.distributing(2)