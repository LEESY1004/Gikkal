from .playgame import PlayGame
from .action import Action #이 파일이 PlayGame안에 있어서 삭제 해도 괜찮을꺼 같음(확인 필요)
from val import CLI_I
from .batting import Batting
import features

def game_start(pl):
    choice = input(CLI_I.GAME_START_MENU)
    if choice == "1":
        pl_count = input("플레이어 수: ")

        pg = PlayGame()
        #action = pg.Action() #이렇게 수정해도 될 듯(확인 필요)
        action=Action()
        betting = Batting()

        pg.play_blackjack_set()

        # 베팅
        betting.get_bet_amount() #betting 돈을 출력하고, betting 전반적인 시스템 호출

        # 플레이어 1
        action.hit_stand(pg, pl)  
        player_value = pg.calculate_hand_value(pg.player_hand)

        if pl_count == "1": # 플레이어가 1명이면 실행
            dealer_value = pg.calculate_hand_value(pg.dealer_hand)

        elif pl_count == "2" or pl_count == "3": # 플레이어가 2,3명이면 실행
            auto_player_values = []  # 자동 플레이어들의 결과를 저장할 리스트
            # 딜러의 규칙을 따라 플레이어 2와 3을 자동으로 생성 및 진행
            for i in range(int(pl_count) - 1):  # 플레이어 1을 제외한 횟수만큼 반복
                auto_pg = PlayGame()
                auto_pg.play_blackjack_set() ### 오류: 이부분에서 문제 발생 딜러한테 계속 카드를 분배함 ###

                #이 부분 deal_rule이랑 겹치는 거 같음 수정 필요
                while auto_pg.calculate_hand_value(auto_pg.dealer_hand) <= 17 and auto_pg.deck.cards:
                    auto_pg.dealer_hand.extend(auto_pg.deck.distributing(1))
                    action.deal_rule(auto_pg)

                auto_player_value = auto_pg.calculate_hand_value(auto_pg.player_hand)
                dealer_value = auto_pg.calculate_hand_value(auto_pg.dealer_hand)

                # 자동 플레이어 결과 저장
                auto_player_values.append(auto_player_value)

                # 자동 플레이어 결과 출력
                result = Result(auto_pg)
                result.result_player(auto_player_value)

        # 플레이어 1의 결과 출력
        result = Result(pg)
        result.result(player_value, dealer_value, auto_player_values)
        betting.update_total_money(result) #betting 결과 반환

    elif choice == "2":
        features.back_to_home(pl)

class Result:
    def __init__(self, pg):
        self.pg = pg

    def result_player(self, player_value=None, dealer_value=None, auto_player_values=None): # 플래그 선언
        #player_value가 매개변수를 통해 주어지면 값이 None이 아님
        if player_value is not None:
            print("플레이어의 카드:", self.pg.player_hand) #직접 플레이어 값 출력
        elif isinstance(auto_player_values, list): #자동 플레이어 값 출력
            for i, value in enumerate(auto_player_values, start=2):
                print(f"자동 플레이어 {i}의 카드:", value)
        elif dealer_value is not None:
            print("딜러의 카드:", self.pg.dealer_hand) #딜러 값 출력

    def result(self, player_value, dealer_value, auto_player_values=None):
        self.result_player(player_value=player_value)

        if dealer_value == player_value or (dealer_value > 21 and player_value > 21):
            print("무승부: 플레이어 {} vs. 딜러 {}".format(player_value, dealer_value))
            return 1
        elif player_value > 21 or (dealer_value <= 21 and dealer_value >= player_value):
            print("패배: 플레이어 {} vs. 딜러 {}".format(player_value, dealer_value))
            return -1
        elif dealer_value > 21 or (player_value <= 21 and player_value > dealer_value):
            print("승리: 플레이어 {} vs. 딜러 {}".format(player_value, dealer_value))
            return 2
