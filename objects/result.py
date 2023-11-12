from .playgame import PlayGame
from .action import Action
from val import CLI_I
from .batting import Batting
import features

def game_start(pl):
    choice = input(CLI_I.GAME_START_MENU)
    if choice == "1":
        pl_count = input("플레이어 수: ")

        pg = PlayGame()
        action = Action()
        betting = Batting()

        pg.play_blackjack_set()

        # 베팅
        betting.get_bet_amount()

        # 플레이어 1
        action.hit_stand(pg, pl)  
        player_value = pg.calculate_hand_value(pg.player_hand)

        if pl_count == "1":
            dealer_value = pg.calculate_hand_value(pg.dealer_hand)

        elif pl_count == "2" or pl_count == "3":
            # 딜러의 규칙을 따라 플레이어 2와 3을 자동으로 생성 및 진행
            for i in range(int(pl_count) - 1):  # 플레이어 1을 제외한 횟수만큼 반복
                auto_pg = PlayGame()
                auto_pg.play_blackjack_set()

                while auto_pg.calculate_hand_value(auto_pg.dealer_hand) <= 17 and auto_pg.deck.cards:
                    auto_pg.dealer_hand.extend(auto_pg.deck.distributing(1))
                    action.deal_rule(auto_pg)

                auto_player_value = auto_pg.calculate_hand_value(auto_pg.player_hand)
                dealer_value = auto_pg.calculate_hand_value(auto_pg.dealer_hand)

                # 자동 플레이어 결과 출력
                result = Result(auto_pg)
                game_result = result.result(auto_player_value, dealer_value, pl_count)
                betting.update_total_money(game_result)

        # 플레이어 1의 결과 출력
        result = Result(pg)
        game_result = result.result(player_value, dealer_value, pl_count)
        betting.update_total_money(game_result)

    elif choice == "2":
        features.back_to_home(pl)



class Result:
    def __init__(self, pg):
        self.pg = pg

    def result(self, player_value, dealer_value, pl_count):
        print("플레이어의 카드:", self.pg.player_hand)
        
        print("딜러의 카드:", self.pg.dealer_hand)

        if dealer_value == player_value or (dealer_value > 21 and player_value > 21):
            print("무승부: 플레이어 {} vs. 딜러 {}".format(player_value, dealer_value))
            return 1
        elif player_value > 21 or (dealer_value <= 21 and dealer_value >= player_value):
            print("패배: 플레이어 {} vs. 딜러 {}".format(player_value, dealer_value))
            return -1
        elif dealer_value > 21 or (player_value <= 21 and player_value > dealer_value):
            print("승리: 플레이어 {} vs. 딜러 {}".format(player_value, dealer_value))
            return 2