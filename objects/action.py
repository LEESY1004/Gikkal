from .playgame import PlayGame
from .card import Card
import features.game as game

class Action:
    def deal_rule(self, playgame):
        # 딜러의 선택 (카드 합이 17 이하일 때 히트)
        while playgame.calculate_hand_value(playgame.dealer_hand) <= 17 and playgame.deck.cards:
            playgame.dealer_hand.extend(playgame.deck.distributing(1))
            
            # 딜러의 A 카드 처리 (A는 11 또는 1로 계산)
            dealer_value = playgame.calculate_hand_value(playgame.dealer_hand)
            num_aces = playgame.dealer_hand.count('A')
            while dealer_value <= 10 and num_aces > 0:
                dealer_value += 10
                num_aces -= 1

                

    def hit_stand(self, playgame, pl):
        while True:
            # 플레이어의 카드 합 계산
            player_value = playgame.calculate_hand_value(playgame.player_hand)
            
            
            # ## !<-- Player가 1명일 때 구현, 작업할 때 아래 코드 주석하고 작업 부탁드립니다. -->

            # cards_arr = []
            # cards = []
            # for c in playgame.player_hand:
            #     card = c.split(':')
            #     cards.append(Card(card[0], card[1]))
            # cards_arr.append(cards)

            # players = [pl]
            # dealer_cards = [Card("Diamonds", "King"), Card("Diamonds", "King"), Card("Diamonds", "King"), Card("Diamonds", "King"), Card("Diamonds", "King"), Card("Diamonds", "King")]
            # game.show_game(dealer_cards, players, cards_arr)

            # ## -->

            print("플레이어의 카드:", playgame.player_hand)
            if player_value > 21:
                print("패배: 플레이어 {} vs. 딜러 {}".format(player_value, playgame.calculate_hand_value(playgame.dealer_hand)))
                break  # 플레이어가 21을 넘으면 패배 처리하고 종료

            if playgame.dealer_hand:
                print("딜러의 카드:", [f"{playgame.dealer_hand[0].split(':')[0]}:{playgame.dealer_hand[0].split(':')[1]}", "알 수 없음"])
            else:
                print("딜러의 카드: 알 수 없음")

            # 플레이어의 선택 (히트 또는 스테이)
            choice = input("히트(1) 또는 스테이(2) 선택: ")
            if choice == '1':
                playgame.player_hand.extend(playgame.deck.distributing(1))  # 히트: 카드 1장 뽑음
                self.deal_rule(playgame)
            elif choice == '2':
                self. deal_rule(playgame)
                break  # 스테이: 게임 종료
        


    










