from deck import Deck
deck=Deck()

class PlayGame:
    def __init__(self):
        self.player_hand = []
        self.dealer_hand = []

    def calculate_hand_value(self, hand):
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

    def play_blackjack(self):
        deck = Deck()
        deck.shuffle()

        # 플레이어와 딜러에게 각각 2장의 카드를 나눠줌
        self.player_hand = deck.distributing(2)
        self.dealer_hand = deck.distributing(2)

    def hit(self):
        while True:
            print("플레이어의 카드:", self.player_hand)
            print("딜러의 카드:", [f"스페이드:{self.dealer_hand[0].split(':')[1]}", "알 수 없음"])  # 딜러의 첫 번째 카드만 공개

            # 플레이어의 선택 (히트 또는 스테이)
            choice = input("히트(1) 또는 스테이(2) 선택: ")
            if choice == '1':
                if not deck.cards:
                    print("덱이 비어 있습니다.")
                    break
                self.player_hand.extend(deck.distributing(1))  # 히트: 카드 1장 뽑음
            elif choice == '2':
                break  # 스테이: 게임 종료

        # 딜러의 선택 (카드 합이 17 이하일 때 히트)
        while self.calculate_hand_value(self.dealer_hand) <= 17 and deck.cards:
            self.dealer_hand.extend(deck.distributing(1))

    def result(self):
        player_value = self.calculate_hand_value(self.player_hand)
        dealer_value = self.calculate_hand_value(self.dealer_hand)
        print("플레이어의 카드:", self.player_hand)
        print("딜러의 카드:", self.dealer_hand)

        if player_value > 21 or (dealer_value <= 21 and dealer_value >= player_value):
            print("패배: 플레이어 {} vs. 딜러 {}".format(player_value, dealer_value))
        elif dealer_value > 21 or (player_value <= 21 and player_value > dealer_value):
            print("승리: 플레이어 {} vs. 딜러 {}".format(player_value, dealer_value))
        else:
            print("무승부: 플레이어 {} vs. 딜러 {}".format(player_value, dealer_value))

# 클래스 인스턴스 생성

game = PlayGame()


game.play_blackjack()
game.hit()
game.result()
