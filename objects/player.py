class Player:
    def __init__(self, name, curr_chip=None, win_c=0, lose_c=0, win_rate=0.0):
        self.name = name
        self.curr_chip = curr_chip if curr_chip is not None else [0, 0, 0, 0, 0, 0]
        self.win_c = win_c
        self.lose_c = lose_c
        self.win_rate = win_rate

    def set_money(self, chips):
        for i in range(6):
            self.curr_chip[i] = chips[i]

    def get_name(self):
        return self.name

    def get_curr_chip(self):
        return self.curr_chip

    def set_curr_chip(self, curr_chip):
        self.curr_chip = curr_chip

    def get_win_c(self):
        return self.win_c

    def set_win_c(self, win_c):
        self.win_c = win_c

    def get_lose_c(self):
        return self.lose_c

    def set_lose_c(self, lose_c):
        self.lose_c = lose_c

    def get_win_rate(self):
        return self.win_rate

    def set_win_rate(self, win_rate):
        self.win_rate = win_rate