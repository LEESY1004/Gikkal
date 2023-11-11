
class Batting:
    def __init__(self):
        self.current_bet = 0
        self.total_money = 1000  # 처음 제공되는 금액

    def get_bet_amount(self):
        while True:
            try:
                bet_amount = int(input("배팅할 금액을 입력하세요 (1~1000): "))
                if 1 <= bet_amount <= 1000 and bet_amount <= self.total_money:
                    self.current_bet = bet_amount
                    return bet_amount
                else:
                    print("1부터 1000 사이의 값을 입력하고 현재 가진 금액 이하로 배팅하세요.")
            except ValueError:
                print("유효한 숫자를 입력하세요.")
    def update_total_money(self, rs):
        if rs == 1:
            self.total_money += self.current_bet  # 무승부
        elif rs == -1:
            self.total_money -= self.current_bet  # 패배
        elif rs == 2:
            self.total_money += (2 * self.current_bet)  # 승리

        print("현재 가진 금액: ${}".format(self.total_money))