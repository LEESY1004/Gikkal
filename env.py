from enum import Enum
class PATH:
    TXT_FILE = './db/txt/'
    CSV_FILE = './db/csv/'
    ZIP_FILE = './db/zip/'

class CLI_I:
    CHOICE_MENU = '''
choice :
----------------------------------------
1. Game Start
2. Show game record
3. Back to home
4. Exit
----------------------------------------
'''

def player_object_to_txt(pl):
    return f'''
Player Info
--------------------------------------
name : {pl.name}
current chip : [{pl.curr_chip[0]} | {pl.curr_chip[1]} | {pl.curr_chip[2]} | {pl.curr_chip[3]} | {pl.curr_chip[4]}]
win count : {pl.win_c}
lose count : {pl.lose_c}
win rate : {pl.win_rate}%
--------------------------------------
'''