import os
import mode_casual.casual_menu as casual_menu
import features 
from objects.player import Player
from env import CLI_I

def init_db(name):
    file_path = features.get_db_file_path(name)
    if os.path.exists(file_path):
        print(f"Sign-in: {name}")
        pl = features.player_txt_to_object(file_path)
        return pl

    print(f"Sign-up: {name}")
    f = open(file_path, "w")
    pl = Player(name)
    f.write(features.player_object_to_txt(pl))
    f.close()
    return pl


def choose_mod(pl):
    mode = input(CLI_I.DB_MENU)
    if mode == "1":
        casual_menu.choice_menu(pl)
    if mode == "2":
        print("Implementing...")
        choose_mod(pl)

def lobby(pl):
    print(features.player_object_to_txt(pl))
    choose_mod(pl)
