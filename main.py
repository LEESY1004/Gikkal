import home
import log

name = input("Please input your name : ")
pl = home.init_db(name)
home.lobby(pl)
