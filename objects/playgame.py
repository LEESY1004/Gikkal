from .deck import Deck


class PlayGame:
    def __init__(self): # 클래스가 인스턴스화 될 때 초기화 작업을 수행하는 함수
        self.player_hand = [] # player_hand에 리스트로 저장
        self.auto_player_hand_1=[] # auto_player_hand_1에 리스트로 저장
        self.auto_player_hand_2=[] # auto_player_hand_2에 리스트로 저장
        self.dealer_hand = [] # dealer_hand에 리스트로 저장
        self.deck = Deck()
        self.betting_taken = False # 플래그 역할을 하는 변수로 처음에는 아직 베팅이 이루어지지 않았기 때문에 False로 설정 
        
        self.auto_player_hand_1=self.deck.distributing(2)
        self.auto_player_hand_2=self.deck.distributing(2)
        self.player_hand = self.deck.distributing(2)
        self.dealer_hand = self.deck.distributing(2)

    def calculate_hand_value(self, hand): # 카드를 int형으로 계산하는 함수
        value = 0
        num_aces = 0

        for card in hand:
            rank = card.split(":")[1].strip() # 카드 문자열에서 숫자 또는 랭크 추출
            if rank.isdigit():
                value += int(rank)
            elif rank in ["King", "Queen", "Jack"]:
                value += 10
            elif rank == "Ace":
                num_aces += 1
                value += 11 

        while num_aces > 0 and value > 21: # Ace를 1로 변경하여 자동으로 버스트를 피하려는 로직
            value -= 10
            num_aces -= 1

        return value
