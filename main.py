import home
from player import Player

name = input("Please input your name : ")
pl = home.init_db(name)
home.lobby(pl)
