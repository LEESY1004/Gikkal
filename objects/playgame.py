from .deck import Deck
from .batting import Batting ###수정


class PlayGame:
    def __init__(self): #클래스가 인스턴스화 될 때 초기화 작업을 수행하는 함수
        self.player_hand = [] # player_hand에 리스트로 저장
        self.dealer_hand = [] # dealer_hand에 리스트로 저장
        self.deck = Deck()
        self.betting_taken = False # 플래그 역할을 하는 변수로 처음에는 아직 베팅이 이루어지지 않았기 때문에 False로 설정 ### 수정
        self.play_blackjack_set() # 객체가 만들어지면 자동으로 실행되도록 설정 

    def calculate_hand_value(self, hand): # 카드를 int형으로 계산하는 함수
        value = 0
        num_aces = 0

        for card in hand:
            rank = card.split(":")[1].strip()  # 카드 문자열에서 숫자 또는 랭크 추출
            if rank.isdigit():
                value += int(rank)
            elif rank in ["King", "Queen", "Jack"]:
                value += 10
            elif rank == "Ace":
                num_aces += 1
                value += 11  # 일단 11로 더하고 나중에 1로 변경할 수 있음

        # Ace를 1로 변경하여 버스트를 피하려는 로직
        while num_aces > 0 and value > 21:
            value -= 10
            num_aces -= 1

        return value

    def play_blackjack_set(self): # 카드 분배
        if not self.betting_taken: #not False니까 현재 상태 True
            # 플레이어와 딜러에게 각각 2장의 카드를 나눠줌
            self.player_hand = self.deck.distributing(2)
            self.dealer_hand = self.deck.distributing(2)