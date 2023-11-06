from objects.player import Player
import pandas as pd
import shutil
import zipfile
import os
from env import PATH

# log 관련 사용할 메서드 모음

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

def player_txt_to_object(file_path):
    f = open(file_path, "r")
    player_info = {}
    lines = f.readlines()
    for i in range(3, 8):
        dic = lines[i].strip().split(":")
        if len(dic) == 2:
            key, value = dic[0].strip(), dic[1].strip()
            player_info[key] = value 
    f.close()

    return Player(
        player_info['name'],
        [int(item) for item in player_info['current chip'].strip("[]").split('|')],
        int(player_info['win count']),
        int(player_info['lose count']),
        float(player_info['win rate'].strip('%')) 
    )

def get_db_file_path(name):
    return f"{PATH.TXT_FILE}{name}_db.txt"

def export_txt_to_csv(name, path):
    read_file = pd.read_csv(path)
    read_file.to_csv(f'{PATH.CSV_FILE}{name}_db.csv', index=None)
    return f'{PATH.CSV_FILE}{name}_db.csv'

def download_all_log_db():
    db_path = PATH.TXT_FILE
    zip_name = "logs.zip"

    for dir_path, dirs, files in os.walk(db_path):
        print(f'''
Select file range. ex) 2 4
----------------------------------------''')
        for file in files:
            file_path = os.path.join(dir_path, file)
            print(file_path)
        print('----------------------------------------')

    try:
        with zipfile.ZipFile(zip_name, 'w', zipfile.ZIP_DEFLATED) as zipf:
            for dir_path, dirs, files in os.walk(db_path):
                for file in files:
                    file_path = os.path.join(dir_path, file)
                    zipf.write(file_path, os.path.relpath(file_path, dir_path))
        
        shutil.move(zip_name, f'{PATH.ZIP_FILE}{zip_name}')
        return f'{PATH.ZIP_FILE}{zip_name}'
    except Exception as e:
        print(f"error: {e}")