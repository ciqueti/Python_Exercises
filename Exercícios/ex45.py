#Game Jokenpo 
from time import sleep
import emoji
import random
print(emoji.emojize('Python is fun? :red_heart:'))
print('-+-'*15)
print('Game Jokenpo')
print(emoji.emojize('[ 1 ] - :oncoming_fist: \n[ 2 ] - :hand_with_fingers_splayed: \n[ 3 ] - :victory_hand:'))
itens = [':oncoming_fist:', ':hand_with_fingers_splayed:', ':victory_hand:']
j1 = int(input('Escolha uma opção: '))
j2 = int(random.randint(1,3))
print('-='*15)
print('JO-', end='')
sleep(1)
print('KEN-', end='')
sleep(1)
print('PO!!')
sleep(1)
print(emoji.emojize(itens[(j1 - 1)]), end='  ')
print('VS', end=' ')
print(emoji.emojize(itens[(j2 - 1)]), end='  ')
if (j1 == j2):
    print('EMPATE')
elif (j1 == 1):
    if(j2 == 2):
        print('J2 ganha')
    else:
        print('J1 ganha')
elif (j1 == 2):
    if(j2 == 1):
        print('J1 ganha')
    else:
        print('J2 ganha')
elif (j1 == 3):
    if(j2 == 1):
        print('J2 ganha')
    else:
        print('J1 ganha')
print('-='*15)
