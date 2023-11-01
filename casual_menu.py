import home

# TODO 2. show game record 구현
# TODO 1. Game Start 구현

def choice_menu(pl):
    menu = input('''
choice :
----------------------------------------
1. Game Start
2. Show game record
3. Back to home
4. Exit
----------------------------------------
''')

    if menu == "1":
        print("..")
    elif menu == "2":
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
