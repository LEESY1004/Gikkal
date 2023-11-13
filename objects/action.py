from .playgame import PlayGame
from .card import (Card, ascii_version_of_hidden_card)
import features.game as game

class Action:
    def deal_rule(self, playgame): 
        # 딜러의 선택 (카드 합이 17 이하일 때 히트)
        while playgame.calculate_hand_value(playgame.dealer_hand) <= 17 and playgame.deck.cards: #playgame을 실행 시키면 카드 분배가 자동으로 되서 dealer_hand와 player_hand가 설정됨
            playgame.dealer_hand.extend(playgame.deck.distributing(1)) # 17이하면 playgame에 import되어있는 deck의 함수 distributing에서 카드를 한장 뽑아라
            dealer_value = playgame.calculate_hand_value(playgame.dealer_hand) # 딜러의 A 카드 처리 (A는 11 또는 1로  자동계산은 이미 playgame.calculate_hand_value에 구현 되어 있음)         

    def hit_stand(self, playgame, pl): #pl가 player수
        while True: #2를 입력해서 스테이 상태가 될 때 까지 무한 반복
            # 플레이어의 카드 합 계산
            player_value = playgame.calculate_hand_value(playgame.player_hand)
            
            ## !<-- Player가 1명일 때 구현, 작업할 때 아래 코드 주석하고 작업 부탁드립니다. -->

            cards_arr = []
            cards = []
            dealer_cards = []
            for c in playgame.player_hand:
                card = c.split(':')
                cards.append(Card(card[0], card[1]))
            cards_arr.append(cards)

            for d in playgame.dealer_hand:
                card = d.split(":")
                dealer_cards.append(Card(card[0], card[1]))

            print(ascii_version_of_hidden_card(*dealer_cards))
            players = [pl]
            game.show_game(dealer_cards, players, cards_arr,False)

            ## -->

        
            if player_value > 21:
                print("패배: 플레이어 {} vs. 딜러 {}".format(player_value, playgame.calculate_hand_value(playgame.dealer_hand)))
                break  # 플레이어가 21을 넘으면 패배 처리하고 종료



            # 플레이어의 선택 (히트 또는 스테이)
            choice = input("히트(1) 또는 스테이(2) 선택: ")
            if choice == '1':
                playgame.player_hand.extend(playgame.deck.distributing(1))  # 히트: 카드 1장 뽑음
            elif choice == '2':
                self.deal_rule(playgame) #플레이어 선택에 따른 딜러의 행동(17이하면 계속 히트)
                game.show_game(dealer_cards, players, cards_arr,True)
                break  # 스테이: 게임 종료
        


    










