import home
import features.game as game
from objects.card import Card
from objects.player import Player

name = input("Please input your name : ")
pl = home.init_db(name)
home.lobby(pl)