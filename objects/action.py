from playgame import PlayGame
play = PlayGame()


class Action:
    def deal_rule(self, playgame):
        # 딜러의 선택 (카드 합이 17 이하일 때 히트)
        while playgame.calculate_hand_value(playgame.dealer_hand) <= 16 and playgame.deck.cards:
            playgame.dealer_hand.extend(playgame.deck.distributing(1))
            
            # 딜러의 A 카드 처리 (A는 11 또는 1로 계산)
            dealer_value = playgame.calculate_hand_value(playgame.dealer_hand)
            num_aces = playgame.dealer_hand.count('A')
            while dealer_value <= 10 and num_aces > 0:
                dealer_value += 10
                num_aces -= 1

    def hit_stand(self, playgame):
        while True:
            # 플레이어의 카드 합 계산
            player_value = playgame.calculate_hand_value(playgame.player_hand)
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
                if not playgame.deck.cards:
                    print("덱이 비어 있습니다.")
                    break
                playgame.player_hand.extend(playgame.deck.distributing(1))  # 히트: 카드 1장 뽑음
                self.deal_rule(playgame)
            elif choice == '2':
                self. deal_rule(playgame)
                break  # 스테이: 게임 종료


    










