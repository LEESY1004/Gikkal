import home
import log
from env import (CLI_I, FILE)
import objects.result as game

def choice_menu(pl):
    menu = input(CLI_I.CHOICE_MENU)
    if menu == "1": # game start
        game.game_start(pl)
    elif menu == "2": # show game record
        num = input(CLI_I.EXPORT_FILE_MENU)
        if num == '1':
            export_file(FILE.CSV, pl.name)
        elif num == '2':
            export_file(FILE.ZIP, pl.name)
        elif num == "3": 
            home.lobby(pl)          
    elif menu == "3": # back to menu
        home.lobby(pl)
    elif menu == "4":
        exit(0)

def export_file(category,  name):
    message = ""
    if category == FILE.CSV:
        message = log.export_txt_to_csv(name, log.get_db_file_path(name))
    elif category == FILE.ZIP:
        message = log.download_all_log(name, log.get_db_file_path(name))
    print(f"Successfully export {category} file!!")
    print(f"{category} file dir: ", message)