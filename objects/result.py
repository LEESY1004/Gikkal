from .playgame import PlayGame
from .action import Action
from val import CLI_I
from .batting import Batting
import features.calc_chip as c
import features.logs as feature_1

def game_start(pl):
    choice = input(CLI_I.GAME_START_MENU)
    if choice == "1":
        pl_count= int(input("플레이어수를 작성해주세요."))
        while True:
            betting = Batting(c.calc_money(pl.get_curr_chip()))
            pg = PlayGame()
            action = Action() 

            #플레이어 카드 분배
            if pl_count==1:
                pg.player_hand = pg.deck.distributing(2)
            if pl_count==2:
                pg.auto_player_hand_1 = pg.deck.distributing(2)
            if pl_count==3:
                pg.auto_player_hand_2 = pg.deck.distributing(2)
            
            #딜러 카드 분배
            pg.dealer_hand = pg.deck.distributing(2)

            # 베팅
            betting.get_bet_amount() #betting 돈을 출력하고, betting 전반적인 시스템 호출

            # 플레이어 행동
            action.hit_stand(pg, pl,pl_count) 

            player_value = pg.calculate_hand_value(pg.player_hand)
            dealer_value = pg.calculate_hand_value(pg.dealer_hand)

            # 플레이어 결과 출력
            result = Result(pg)
            rs = result.result(player_value, dealer_value)
            betting.update_total_money(rs, pl) #betting 결과 반환
            
            play_again = input("게임을 더 하시겠습니까? (y/n): ")
            if play_again.lower() != 'y':
                print("게임을 종료합니다.")
                break

    elif choice == "2":
        feature_1.back_to_home(pl)

class Result:
    def __init__(self, pg):
        self.pg = pg

    def result_player(self, player_value=None, dealer_value=None, auto_player_values=None): # 플래그 선언  ### 삭제 예정
        #player_value가 매개변수를 통해 주어지면 값이 None이 아님 
        print("딜러의 카드:", self.pg.dealer_hand) #딜러 값 출력
        print("플레이어의 카드:", self.pg.player_hand) #직접 플레이어 값 출력

    def result(self, player_value, dealer_value, auto_player_values=None):
        self.result_player(player_value=player_value) #카드값 출력

        if dealer_value == player_value or (dealer_value > 21 and player_value > 21):
            print("무승부: 플레이어 {} vs. 딜러 {}".format(player_value, dealer_value))
            return 1
        elif (dealer_value <= 21 and dealer_value >= player_value):
            print("패배: 플레이어 {} vs. 딜러 {}".format(player_value, dealer_value))
            return -1
        elif dealer_value > 21 or (player_value <= 21 and player_value > dealer_value):
            print("승리: 플레이어 {} vs. 딜러 {}".format(player_value, dealer_value))
            return 2
        
