from objects.player import Player
import pandas as pd
import shutil
import zipfile
import os
from env import PATH, INFO

# log 관련 사용할 메서드 모음

def player_object_to_txt(pl):
    return f'''
Player Info
--------------------------------------
{INFO.NAME} : {pl.name}
{INFO.CURRENT_CHIP} : [{pl.curr_chip[0]} | {pl.curr_chip[1]} | {pl.curr_chip[2]} | {pl.curr_chip[3]} | {pl.curr_chip[4]}]
{INFO.WIN_COUNT} : {pl.win_c}
{INFO.LOSE_COUNT} : {pl.lose_c}
{INFO.WIN_RATE} : {pl.win_rate}%
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
        player_info[INFO.NAME],
        [int(item) for item in player_info[INFO.CURRENT_CHIP].strip("[]").split('|')],
        int(player_info[INFO.WIN_COUNT]),
        int(player_info[INFO.LOSE_COUNT]),
        float(player_info[INFO.WIN_RATE].strip('%')) 
    )

def get_db_file_path(name):
    return f"{PATH.TXT_FILE}{name}{PATH.TXT_ET}"

def export_txt_to_csv(name, path):
    read_file = pd.read_csv(path)
    read_file.to_csv(f'{PATH.CSV_FILE}{name}{PATH.CSV_ET}', index=None)
    return f'{PATH.CSV_FILE}{name}{PATH.CSV_ET}'

def download_all_log(name, path):
    db_path = path
    zip_name = f"logs_{name}.zip"
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