class Player:
    def __init__(self, name, curr_chip=None, win_c=0, lose_c=0, win_rate=0.0):
        self.name = name
        self.curr_chip = curr_chip if curr_chip is not None else [0, 0, 0, 0, 0]
        self.win_c = win_c
        self.lose_c = lose_c
        self.win_rate = win_rate
    