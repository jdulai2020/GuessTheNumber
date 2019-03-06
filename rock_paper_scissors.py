#!/usr/bin/env python3

from random import randint

player = input('rock(r), paper(p), or scissors(s)? ')
print(player, 'vs ', end='')
chosen = randint(1,3)
if chosen == 1:
    computer = 'r'
elif chosen == 2:
    computer = 'p'
else:
    computer = 's'
print(computer)

if player == computer:
    print('Draw')
elif player == 'r' and computer == 'p' or player == 's' and computer == 'p' or player == 'p' and computer == 'r':
    print('You Win!')
elif player == 'p' and computer == 'r' or player == 'p' and computer == 's' or player == 'r' and computer == 'p':
    print('You Lost!')
