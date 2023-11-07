import home
import features

name = input("Please input your name : ")
pl = home.init_db(name)
home.lobby(pl)

# pl.set_money(log.calc_chip(10000000))
# log.player_info_update(pl)