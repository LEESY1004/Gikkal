import features.logs as f
import features.calc_chip as c

class Betting:
    def __init__(self, curr_money):
        self.current_bet = 0
        self.total_money = curr_money
        self.bet_taken = False  # 플래그 설정

    def get_bet_amount(self):
        if not self.bet_taken:  # 플래그 활용
            try:
                bet_amount = int(input("Input bet price: (1~1000): "))
                if 1 <= bet_amount <= 1000 and bet_amount <= self.total_money:
                    self.current_bet = bet_amount
                    self.total_money -= bet_amount
                    self.bet_taken = True
                    return bet_amount
                else:
                    print("Enter a value between 1 and 1000 and bet below the current amount.")
                    return self.get_bet_amount()  # 재귀 호출로 다시 입력 받음
            except ValueError:
                print("Please input valid value.")
                return self.get_bet_amount()  # 재귀 호출로 다시 입력 받음

    def update_total_money(self, result, pl):
        if result == 1:
            self.total_money += self.current_bet * 1
        elif result == -1:
            self.total_money += self.current_bet * 0
        elif result == 2:
            self.total_money += self.current_bet * 2
        pl.set_money(c.calc_chip(self.total_money))
        f.player_info_update(pl)
        print("Current money:", (self.total_money))
        self.bet_taken = False  # 다시 betting 끝나면 초기화
