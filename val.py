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
4. Explain rule
5. Exit
----------------------------------------
'''
    DB_MENU = '''
Choice game mode
----------------------------------------
1. Casual
2. !Basic! (Not yet...)
3. show money($)
----------------------------------------
'''

    EXPORT_FILE_MENU = '''
1. Export CSV File
2. Export Zip File
3. Back to home
'''
    GAME_START_MENU = '''
----------------------------------------
1. Select Player Count and Game Start  
2. Back to home
'''

    EXPLAIN_RULE = '''

주요 용어

1. Hit(히트)- 카드 1장 추가, Stay(스테이)- 카드 더 받지 않음.
2. Burst(버스트): 플레이어 또는 딜러의 카드 합이 21을 초과한 경우⇒ 패
3. push(푸시): 플레이어와 딜러 카드 합이 같은 경우⇒ 무승부

기본 규칙:

1.블랙잭은 각 플레이어(1명 이상)와 딜러의 경쟁입니다.
2. 각자 최종 카드들의 합이 21과 같거나 가장 가까운 사람이 승리합니다. (초과(버스트)시, 패배)
    - 무승부(푸시)시, 배팅금액은 본인에게 그대로 돌아갑니다.
3. 카드 계산: 숫자 2~9는 고유 숫자 그대로, 10/J/Q/K는 모두 값 10으로 통일합니다.
    - A는 숫자 1 or 11 중 택 1이나, 해당 프로그램에서는 11이 자동 적용된 후 만일 11이 더해진 합이 21을 초과할시, 1 적용으로 바뀝니다.
4. 처음에 카드를 2장씩 받으며, 딜러는 두 카드 중 하나만 플레이어들에게 공개됩니다.
5. 이후, 플레이어가 히트 혹은 스테이를 선택하면 딜러도 히트 혹은 스테이를 선택하되 플레이어는 그 여부를 알 수 없습니다.
6. 딜러도 히트 혹은 스테이를 선택했다면, 해당 판은 끝나고 모두의 카드가 공개됩니다. 따라서, 승패 여부가 결정됩니다.
    '''