import objects.card as cardOb

# print cards to rows
def sort_card_row(cards, start_padding = ''):
    cat_card = [[] for i in range(9)]
    width_each_card = ' '
    ranges = [(0, 11), (12, 23), (24, 35), (36, 47), (48, 59), (60, 71), (72, 83), (84, 95), (96, 107)]
    for i in range(9):
        for card in cards:
            for j in range(ranges[i][0], ranges[i][1]):
                cat_card[i].append(cardOb.ascii_version_of_card(card)[j])
            cat_card[i].append(width_each_card)

    print_cards(cat_card, start_padding)

# print dealers, players card in terminal
def show_game(dealer_cards, players, cards_arr,flag):
    dealer_padding = '\t' * 13
    dealer_margin = '\n' * 3
    single_player_card_padding = {1: '\t' * 12 + ' ' * 6, 
                                  2: '\t' * 12, 
                                  3: '\t' * 11 + ' ' * 2, 
                                  4: '\t' * 10 + ' ' * 3, 
                                  5: '\t' * 9 + ' ' * 6, 
                                  6: '\t' * 8 + ' ' * 7}
    
    if flag==True:
        # padding
        single_player_card_print(dealer_padding, 'Dealer', dealer_cards, single_player_card_padding[len(dealer_cards)])
        print(dealer_margin)

    if len(players) == 1:
        single_player_card_print(dealer_padding, players[0].name, cards_arr[0], single_player_card_padding[len(cards_arr[0])])
    else: padding_card_arr(players, cards_arr)

def padding_card_arr(players, cards_arr):
    cat_card = [[] for i in range(9)]
    width_each_card = ' '
    ranges = [(0, 11), (12, 23), (24, 35), (36, 47), (48, 59), (60, 71), (72, 83), (84, 95), (96, 107)]

    multi_player_start_margin = {1: '\t' * 5 + ' ' * 2,
                                2: '\t' * 4 + ' ' * 3,
                                3: '\t' * 3 + ' ' * 6,
                                4: '\t' * 3,
                                5: '\t' * 2 + ' ' * 2,
                                6: '\t' * 1 + ' ' * 3}

    multi_player_each_margin = {2: '\t' * 13,
                                3: '\t' * 9 + ' ' * 3}

    if len(players) == 2:
        print(multi_player_start_margin[len(players)], end='')
        print(players[0].name, end='')
        print()
    elif len(players) == 3:
        print(multi_player_start_margin[len(players)], end='')
        print(players[0].name, end='')

        print(multi_player_each_margin[len(players)], end='')
        
        print(players[1].name, end='')

        print(multi_player_each_margin[len(players)], end='')
        
        print(players[2].name, end='')
        
        print()

    for q in range(len(cards_arr)):
        for i in range(9):
            for card in cards_arr[q]:
                for j in range(ranges[i][0], ranges[i][1]):
                    cat_card[i].append(cardOb.ascii_version_of_card(card)[j])
                cat_card[i].append(width_each_card)
            
            cat_card[i].append(multi_player_each_margin[len(cards_arr)] + '\b' * (len(cards_arr[q])*10))
            
    print_cards(cat_card, multi_player_start_margin[len(cards_arr)])


def print_cards(cards, start_margin):
    for card in cards:
        print(start_margin, end="")
        for j in card:
            print(j, end="")
        print()

def single_player_card_print(player_padding, name, cards, card_padding):
    print(player_padding,  end='')
    print(name)
    sort_card_row(cards, card_padding)
