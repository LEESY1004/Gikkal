from .playgame import PlayGame
from .card import (Card, ascii_version_of_hidden_card)
import features.game as game
from .player import Player

class Action:
    def deal_rule(self, playgame): # 딜러의 선택 (카드 합이 17 이하일 때 히트)
        while playgame.calculate_hand_value(playgame.dealer_hand) <= 17 and playgame.deck.cards: # playgame을 실행 시키면 카드 분배가 자동으로 되서 dealer_hand와 player_hand가 설정됨
            playgame.dealer_hand.extend(playgame.deck.distributing(1)) # 17이하면 playgame에 import되어있는 deck의 함수 distributing에서 카드를 한장 뽑아라 

    def auto_player_rule_1(self, playgame): 
        while playgame.calculate_hand_value(playgame.auto_player_hand_1) <= 17 and playgame.deck.cards: 
            playgame.auto_player_hand_1.extend(playgame.deck.distributing(1)) 

    def auto_player_rule_2(self, playgame): 
        while playgame.calculate_hand_value(playgame.auto_player_hand_2) <= 17 and playgame.deck.cards: 
            playgame.auto_player_hand_2.extend(playgame.deck.distributing(1))  

    def hit_stand(self, playgame, pl, pl_count): 
        while True: 
            for i in range(0,pl_count,1): # 플레이어의 카드 합 계산
                player_value = playgame.calculate_hand_value(playgame.player_hand)
                cards_arr = []
                ap1_arr=[]
                ap2_arr=[]
                cards = []
                dealer_cards = []
                auto_player_card_1=[]
                auto_player_card_2=[]
                
                for c in playgame.player_hand:
                    card = c.split(':')
                    cards.append(Card(card[0], card[1]))
                cards_arr.append(cards)
                players = [pl]
                
                if pl_count>=2: 
                    for c in playgame.auto_player_hand_1:
                        card = c.split(':')
                        auto_player_card_1.append(Card(card[0], card[1]))
                    cards_arr.append(auto_player_card_1)
                    auto_player_1 = Player('AP1')
                    players = [pl,auto_player_1]
                    if pl_count == 3: 
                        for c in playgame.auto_player_hand_2:
                            card = c.split(':')
                            auto_player_card_2.append(Card(card[0], card[1]))
                        cards_arr.append(auto_player_card_2)
                        auto_player_2 = Player('AP2')
                        players = [pl,auto_player_1,auto_player_2]

                for d in playgame.dealer_hand:
                    card = d.split(":")
                    dealer_cards.append(Card(card[0], card[1]))

            print(ascii_version_of_hidden_card(*dealer_cards), '\n'*4)
            game.show_game(dealer_cards, players, cards_arr, False)    

            if player_value > 21:
                print("Your Lose! : Player {} vs. Dealer {}".format(player_value, playgame.calculate_hand_value(playgame.dealer_hand)))
                break  # 플레이어가 21을 넘으면 패배 처리하고 즉시 종료
            choice = input("hit(1) or stay(2): ") # 플레이어의 선택 (히트 또는 스테이)
            
            if choice == '1':
                playgame.player_hand.extend(playgame.deck.distributing(1))  # 히트: 카드 1장 뽑음
            elif choice == '2':
                self.deal_rule(playgame) # 플레이어 선택에 따른 딜러의 행동(17이하면 계속 히트)
                self.auto_player_rule_1(playgame)
                self.auto_player_rule_2(playgame)
                for c in playgame.dealer_hand[2:]:
                    card = c.split(':')
                    dealer_cards.append(Card(card[0], card[1]))
                for c in playgame.auto_player_hand_1[2:]:
                    card = c.split(':')
                    auto_player_card_1.append(Card(card[0], card[1]))
                for c in playgame.auto_player_hand_2[2:]:
                    card = c.split(':')
                    auto_player_card_2.append(Card(card[0], card[1]))
                game.show_game(dealer_cards, players, cards_arr, True)
                break  # 스테이: 게임 종료

                
                
        


    










