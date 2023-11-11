import home
import features.game as game
from objects.card import Card
from objects.player import Player

name = input("Please input your name : ")
pl = home.init_db(name)
home.lobby(pl)

# dealer_cards = [Card("Diamonds", "King"), Card("Diamonds", "King"), Card("Diamonds", "King"), Card("Diamonds", "King"), Card("Diamonds", "King"), Card("Diamonds", "King")]
# cards1 = [Card("Diamonds", "King"),Card("Diamonds", "King"),Card("Diamonds", "King"), Card("Diamonds", "King"), Card("Diamonds", "King")]
# cards2 = [Card("Diamonds", "Jack"), Card("Diamonds", "Jack"),Card("Diamonds", "Jack"), Card("Diamonds", "Jack"), Card("Diamonds", "King"), Card("Diamonds", "King")]
# cards3 = [Card("Diamonds", "Jack"), Card("Diamonds", "7"), Card("Diamonds", "6"), Card("Diamonds", "King"), Card("Diamonds", "King")]

# cards = []
# cards.append(cards1)
# cards.append(cards2)
# cards.append(cards3)

# pl1 = Player('player1')
# pl2 = Player('player2')
# pl3 = Player('player3')
# players = [pl1, pl2, pl3]

# # 이렇게 바꾸기
# # player_cards = {(pl1, cards1), (pl2, cards2)}

# game.show_game(dealer_cards, players, cards)
# # game.show_game(players, cards_arr)