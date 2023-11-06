from playgame import PlayGame
play = PlayGame()


class Action:
    def hit_stand(self, playgame):
        while True:
            print("플레이어의 카드:", playgame.player_hand)
            if playgame.dealer_hand:
                print("딜러의 카드:", [f"스페이드:{playgame.dealer_hand[0].split(':')[1]}", "알 수 없음"])
            else:
                print("딜러의 카드: 알 수 없음")

            # 플레이어의 선택 (히트 또는 스테이)
            choice = input("히트(1) 또는 스테이(2) 선택: ")
            if choice == '1':
                if not playgame.deck.cards:
                    print("덱이 비어 있습니다.")
                    break
                playgame.player_hand.extend(playgame.deck.distributing(1))  # 히트: 카드 1장 뽑음
            elif choice == '2':
                break  # 스테이: 게임 종료

    def deal_rule(self, playgame):
        # 딜러의 선택 (카드 합이 17 이하일 때 히트)
        while playgame.calculate_hand_value(playgame.dealer_hand) <= 16 and playgame.deck.cards:
            playgame.dealer_hand.extend(playgame.deck.distributing(1))






