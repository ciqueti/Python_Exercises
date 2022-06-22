#Exercício Python 61: Refaça o DESAFIO 51, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando a estrutura while.
print('Gerador de PA')
n = float(input('Primeiro Termo: '))
k = float(input('Razão da PA: '))
an = n + 9*k
while(n!= an):
    print('{} -> '.format(n),end='')
    n = n + k
print(an)