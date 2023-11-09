# White: 1$ | 5%
# Pink: 2$50¢ | 5%
# Red: 5$ | 10%
# Blue: 10$ | 20%
# Green: 25$ | 30%
# Black: 100$ | 30%
def calc_chip(money):
    return [(int)((money * 0.3) / 100),
            (int)((money * 0.3) / 25),
            (int)((money * 0.2) / 10),
            (int)((money * 0.1) / 5),
            (int)((money * 0.05) / 2.5),
            (int)((money * 0.05) / 1)]

def calc_money(chips): #calc_money(chips) => chips배열 받아 money($)로 반환함
    return (chips[0] * 100) + (chips[1] * 25) + (chips[2] * 10) + (chips[3] * 5) + (chips[4] * 2.5) + (chips[5] * 1)
