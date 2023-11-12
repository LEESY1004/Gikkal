
class Batting:
    def __init__(self):
        self.current_bet = 0
        self.total_money = 1000
        self.bet_taken = False

    def get_bet_amount(self):
        if not self.bet_taken:
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

    def update_total_money(self, result):
        if result == 1:
            self.total_money +=self.current_bet*1
        elif result == -1:
            self.total_money += self.current_bet*-1
        elif result == 2:
            self.total_money += self.current_bet*2

        print("현재 가진 금액: ${}".format(self.total_money))
        self.bet_taken = False