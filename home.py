import os
import mode_casual.casual_menu as casual_menu
import features.logs as logs 
import features.calc_chip as calc
from objects.player import Player
from val import CLI_I

def init_db(name):
    file_path = logs.get_db_file_path(name)
    if os.path.exists(file_path):
        print(f"Sign-in: {name}")
        pl = logs.player_txt_to_object(file_path)
        return pl

    print(f"Sign-up: {name}")
    f = open(file_path, "w")
    pl = Player(name, [10, 0, 0, 0, 0, 0])
    
    f.write(logs.player_object_to_txt(pl))
    f.close()
    return pl


def choose_mod(pl):
    mode = input(CLI_I.DB_MENU)
    if mode == "1":
        casual_menu.choice_menu(pl)
    elif mode == "2":
        print("Implementing...")
        choose_mod(pl)
    elif mode == "3":
        print('current money: ', (int)(calc.calc_money(pl.get_curr_chip())),'$')
        choose_mod(pl)

def lobby(pl):
    print(logs.player_object_to_txt(pl))
    choose_mod(pl)
