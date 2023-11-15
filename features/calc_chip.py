# Chip rate
# White: 1$
# Pink: 2$
# Red: 5$
# Blue: 10$
# Green: 25$
# Black: 100$

def calc_chip(money):
    values = [100, 25, 10, 5, 2, 1]
    chips = [0] * len(values)

    for i in range(len(values)):
        chips[i] = (int)(money // values[i])
        money %= values[i]

    return chips

def calc_money(chips): #calc_money(chips) => chips배열 받아 money($)로 반환함
    return (int)((chips[0] * 100) + (chips[1] * 25) + (chips[2] * 10) + (chips[3] * 5) + (chips[4] * 2.5) + (chips[5] * 1))
