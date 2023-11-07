from .playgame import PlayGame
from .action import Action

def game_start(pl):
    pg = PlayGame()
    action = Action()
    pg.play_blackjack_set()
    action.hit_stand(pg)  # Action 클래스의 메소드 호출 시 PlayGame 인스턴스를 전달
    player_value = pg.calculate_hand_value(pg.player_hand)
    dealer_value = pg.calculate_hand_value(pg.dealer_hand)
    result = Result(pg)
    result.result(player_value, dealer_value)

class Result:
    def __init__(self, pg):
        self.pg = pg
    def result(self, player_value, dealer_value):
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
