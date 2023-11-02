from objects.player import Player
import pandas as pd
import shutil
import zipfile
import os

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
    return f"./db/{name}_db.txt"

def export_txt_to_csv(name, path):
    print(path)
    read_file = pd.read_csv(path)
    print(read_file)
    read_file.to_csv(f'./db/csv/{name}_db.csv', index=None)

def download_all_log(directory_path):
    try:
        with zipfile.ZipFile('logs.zip', 'w', zipfile.ZIP_DEFLATED) as zipf:
            for dir_path, dirs, files in os.walk(directory_path):
                for file in files:
                    file_path = os.path.join(dir_path, file)
                    zipf.write(file_path, os.path.relpath(file_path, dir_path))
        
        shutil.move('logs.zip', './db/logs.zip')
        print("Success")
    except Exception as e:
        print(f"error: {e}")