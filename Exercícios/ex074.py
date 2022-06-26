#Exercício Python 074: Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla. Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.
from random import randint
n = (randint(0,10),randint(0,10),randint(0,10),randint(0,10),randint(0,10))
print(f'Os valores sorteados foram', end=' ')
for i in n:
    print(i, end=' ')
print(f'\nO maior valor é {max(n)}')
print(f'O menor valor é {min(n)}')
# print(f'\nO menor valor é {sorted(n)[0]}')
# print(f'O maior valor é {sorted(n)[-1]}')
