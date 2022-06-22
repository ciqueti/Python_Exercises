#Exercício Python 068: Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador perder, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo. 
from random import randint
cont = 0
print('Vamos jogar Par ou Ímpar')
while True:
    p = ' '
    while p not in 'PI':
        p = str(input('[P / I] - ')).upper().strip()[0]
    n = int(input('Que número deseja -'))
    pc = randint(0,10)
    if ((pc + n)%2 == 0):
        res = 'Par'
    else: res = 'Impar'
    print(f'Vocë jogou {n} e o computador {pc}, total é {n + pc} que é {res}')
    if (res[0] == p):
        cont += 1
        print('Voce Ganhou')
    else:
        print(f'Game Over - N de vitórias {cont}')
        break
    print('Vamos Jogar Novamente')