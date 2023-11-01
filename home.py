import os
import casual_menu
import log 
from player import Player


def init_db(name):
    file_path = f"./db/{name}_db.txt"
    if os.path.exists(file_path):
        # 추후 pw검증 개발
        print(f"Sign-in: {name}")
        pl = player_txt_to_object(file_path)
        return pl

    print(f"Sign-up: {name}")
    f = open(file_path, "w")
    pl = Player(name)
    f.write(log.player_object_to_txt(pl))
    f.close()
    return pl

def player_txt_to_object(file_path):

    f = open(file_path, "r")
    pl = log.player_txt_to_object(f.readlines())
    f.close()
    return pl

def choose_mod():
    mode = input('''
Choice game mode
----------------------------------------
1. Casual
2. !Basic! (Not yet...)
----------------------------------------
''')
    if mode == "1":
        casual_menu.choice_menu()

def lobby(pl):
    print(log.player_object_to_txt(pl))
    choose_mod()
