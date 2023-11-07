from enum import Enum
class PATH:
    TXT_FILE = './db/txt/'
    CSV_FILE = './db/csv/'
    ZIP_FILE = './db/zip/'
    TXT_ET = '_db.txt'
    CSV_ET = '_db.csv'
    ZIP_ET = '_db.zip'

class INFO:
    NAME = 'name'
    CURRENT_CHIP = 'current chip'
    WIN_COUNT = 'win count'
    LOSE_COUNT = 'lose count'
    WIN_RATE = 'win rate'

class FILE:
    CSV = 'Csv'
    ZIP = 'Zip'
    TXT = 'Txt'

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
    DB_MENU = '''
Choice game mode
----------------------------------------
1. Casual
2. !Basic! (Not yet...)
----------------------------------------
'''

    EXPORT_FILE_MENU = '''
1. Export CSV File
2. Export Zip File
3. Back to menu
'''