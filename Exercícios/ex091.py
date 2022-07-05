#Exercício Python 091: Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. Guarde esses resultados em um dicionário em Python. No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.
from random import randint
from time import sleep
from operator import itemgetter
resultado = {}
ranking = {}
for i in range(0,4):
    resultado[f'Jogador{i}'] = randint(1,6)
print('=='*10,'JOGANDO O DADO','=='*10)
for k, v in resultado.items():
    print(f'{k} - {v}')
    sleep(1)
ranking = sorted(resultado.items(), key=itemgetter(1),reverse=True)
print('=='*15,'RANKING','=='*15)
for k, v in enumerate(ranking):
    print(f'{k+1}o. {v[0]} | Resultado {v[1]} ')
