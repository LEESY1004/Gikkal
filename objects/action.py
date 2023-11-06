from playgame import PlayGame


class Action:
     
    def hit_stand(self):
        while True:
            print("플레이어의 카드:", self.player_hand)
            print("딜러의 카드:", [f"스페이드:{self.dealer_hand[0].split(':')[1]}", "알 수 없음"])  # 딜러의 첫 번째 카드만 공개

            # 플레이어의 선택 (히트 또는 스테이)
            choice = input("히트(1) 또는 스테이(2) 선택: ")
            if choice == '1':
                if not deck.cards:
                    print("덱이 비어 있습니다.")
                    break
                self.player_hand.extend(deck.distributing(1))  # 히트: 카드 1장 뽑음
            elif choice == '2':
                break  # 스테이: 게임 종료

action=Action()
action.hit_stand()
action.deal_rule()