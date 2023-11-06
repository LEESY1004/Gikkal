from playgame import PlayGame
from action import Action

playgame = PlayGame()
action = Action()

playgame.play_blackjack_set()
action.hit_stand(playgame)  # Action 클래스의 메소드 호출 시 PlayGame 인스턴스를 전달

player_value = playgame.calculate_hand_value(playgame.player_hand)
dealer_value = playgame.calculate_hand_value(playgame.dealer_hand)


class Result:
    def result(self, player_value, dealer_value):
        print("플레이어의 카드:", playgame.player_hand)
        print("딜러의 카드:", playgame.dealer_hand)

        if dealer_value == player_value or (dealer_value > 21 and player_value > 21):
            print("무승부: 플레이어 {} vs. 딜러 {}".format(player_value, dealer_value))
        elif player_value > 21 or (dealer_value <= 21 and dealer_value >= player_value):
            print("패배: 플레이어 {} vs. 딜러 {}".format(player_value, dealer_value))
        elif dealer_value > 21 or (player_value <= 21 and player_value > dealer_value):
            print("승리: 플레이어 {} vs. 딜러 {}".format(player_value, dealer_value))

result = Result()
result.result(player_value, dealer_value)
