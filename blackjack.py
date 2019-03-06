#!/usr/bin/env python3
import random

dealer_cards = []

player_cards = []

while len(dealer_cards) != 2:
     dealer_cards.append(random.randint(1,11))
     if len(dealer_cards) == 2:
         print('Dealer has a', dealer_cards[1])

while len(player_cards) != 2:
    player_cards.append(random.randint(1,11))
    if len(player_cards) == 2:
        print('You have', player_cards[0], '&', player_cards[1])

if sum(dealer_cards) == 21:
    print('Dealer has 21. You Lost!')
elif sum(dealer_cards) > 21:
    print('Dealer busts. You Win!')

while sum(player_cards) < 21:
    hit = input('Do you want to hit? [y/n] ')
    if hit == 'y':
        player_cards.append(random.randint(1,11))
        print('You now have a total of', sum(player_cards))
    else:
        print('Dealer has a total of', sum(dealer_cards))
        print('You have a total of', sum(player_cards))
        if sum(dealer_cards) > sum(player_cards):
            print('You Lost!')
        else:
            print('You Won!')
            break

if sum(player_cards) > 21:
    print('You Bust!')
elif sum(player_cards) == 21:
    print('You Win!')
