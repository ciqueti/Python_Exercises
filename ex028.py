#Escreva um programa que faça o computador “pensar” em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.
from random import randint
from time import sleep
#random.seed()
#print(random.random())
#print(random.random())
n = randint(0, 5)
print('-=-'*20)
m = int(input('Pensei em um número, tente adivinhar... (0 ä 5): '))

print('PROCESSANDO.....')
sleep(2)
if n == m:
    print('Parabéns, vocë acertou o número {}'.format(n))
else:
    print('Que pena, vocë escolheu {}, eu escolhi o {}'.format(m,n))
print('-=-'*20)