from .playgame import PlayGame
from .action import Action
from val import CLI_I
from .betting import Betting
import features.calc_chip as c
import features.logs as feature_1

def game_start(pl):
    choice = input(CLI_I.GAME_START_MENU)
    if choice == "1":
        pl_count= int(input("Player Count(1~3): "))
        while True:
            betting = Betting(c.calc_money(pl.get_curr_chip()))
            pg = PlayGame()
            action = Action() 

            if pl_count==1: #플레이어 수에 따른 카드 분배-플레이어가 1명
                pg.player_hand = pg.deck.distributing(2)
            if pl_count==2: #플레이어 수에 따른 카드 분배-플레이어가 2명
                pg.auto_player_hand_1 = pg.deck.distributing(2)
            if pl_count==3: #플레이어 수에 따른 카드 분배-플레이어가 3명
                pg.auto_player_hand_2 = pg.deck.distributing(2)
            
            pg.dealer_hand = pg.deck.distributing(2) # 딜러 카드 분배

            betting.get_bet_amount() # betting 전반적인 시스템 호출

            action.hit_stand(pg, pl,pl_count) # 플레이어 행동(히트, 스테이)

            player_value = pg.calculate_hand_value(pg.player_hand)
            dealer_value = pg.calculate_hand_value(pg.dealer_hand)

            result = Result(pg) # 플레이어 결과 출력
            rs = result.result(player_value, dealer_value, pl)
            betting.update_total_money(rs, pl) # betting 결과 반환
            
            play_again = input("Continue Game? (y/n): ")
            if play_again.lower() != 'y':
                print("Bye.")
                break

    elif choice == "2":
        feature_1.back_to_home(pl)

class Result:
    def __init__(self, pg):
        self.pg = pg

    def result(self, player_value, dealer_value, pl, auto_player_values=None):
        if dealer_value == player_value or (dealer_value > 21 and player_value > 21):
            print("Draw! : Player {} vs. Dealer {}".format(player_value, dealer_value))
            return 1
        elif (dealer_value <= 21 and dealer_value >= player_value):
            self.player_win_lose_update(pl, False)
            print("Lose! : Player {} vs. Dealer {}".format(player_value, dealer_value))
            return -1
        elif dealer_value > 21 or (player_value <= 21 and player_value > dealer_value):
            self.player_win_lose_update(pl, True)
            print("Win! : Player {} vs. Dealer {}".format(player_value, dealer_value))
            return 2
        
    def player_win_lose_update(self, pl, isWin):
        if isWin:
            pl.set_win_c(pl.get_win_c() + 1)
        else:
            pl.set_lose_c(pl.get_lose_c() + 1)

        total_game = pl.get_win_c() + pl.get_lose_c()
       
        if total_game > 0: # 0으로 나누는 경우를 피하는 코드
            pl.set_win_rate((pl.get_win_c() / total_game) * 100.0)
        else:
            pl.set_win_rate(0.0)
        feature_1.player_info_update(pl)
