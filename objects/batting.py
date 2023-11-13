import features.logs as f
import features.calc_chip as c

class Batting:
    def __init__(self, curr_money):
        self.current_bet = 0
        self.total_money = curr_money
        self.bet_taken = False # 플래그 설정

    def get_bet_amount(self):
        if not self.bet_taken: # 플래그 활용
            try:
                bet_amount = int(input("배팅할 금액을 입력하세요 (1~1000): "))
                if 1 <= bet_amount <= 1000 and bet_amount <= self.total_money:
                    self.current_bet = bet_amount
                    self.total_money -=bet_amount
                    self.bet_taken = True
                    return bet_amount
                else:
                    print("1부터 1000 사이의 값을 입력하고 현재 가진 금액 이하로 배팅하세요.")
                    return self.get_bet_amount()  # 재귀 호출로 다시 입력 받음
            except ValueError:
                print("유효한 숫자를 입력하세요.")
                return self.get_bet_amount()  # 재귀 호출로 다시 입력 받음

    def update_total_money(self, result, pl):
        if result == 1:
            self.total_money +=self.current_bet*1
        elif result == -1:
            self.total_money += self.current_bet*0
        elif result == 2:
            self.total_money += self.current_bet*2

        # Player Money Update Logic
        self.total_money = c.calc_chip(self.total_money)
        pl.set_money(self.total_money)
        f.player_info_update(pl)

        print("현재 가진 금액:",(int)(c.calc_money(self.total_money)))
        self.bet_taken = False #다시 bet 끝나면 초기화