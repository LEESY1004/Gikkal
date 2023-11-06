import home
import log
from env import CLI_I
# TODO 2. show game record 구현
# TODO 1. Game Start 구현

def choice_menu(pl):
    menu = input(CLI_I.CHOICE_MENU)

    if menu == "1":
        print("..")
    elif menu == "2":
        # TODO Export CSV file, Export zip file 두개 만들기
        num = input("1: Export CSV File\n2: Export Zip File\n")
        if num == '1':
            message = log.export_txt_to_csv(pl.name, log.get_db_file_path(pl.name))
            print("Successfully export csv file!!")
            print("dir: ", message)

        elif num == '2':
            log.download_all_log_db()
        print("..")
    elif menu == "3":
        home.lobby(pl)
    elif menu == "4":
        exit(0)


def game_start():
    print("..")
def show_game_record():
    print("..")
def back_to_home():
    print("..")
