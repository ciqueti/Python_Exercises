#Exercício Python 088: Faça um programa que ajude um jogador da MEGA SENA a criar palpites.O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.
from random import randint
from time import sleep
auxiliar = []
principal = []
n = int(input('Quantos jogos da Mega Sena deseja gerar? '))
for k in range(0,n):
    while len(auxiliar)!= 6: #Gerando um jogo - S/ Repetição em (0,60) e 6 Dígitos
        k = randint(0,60)
        if k not in auxiliar:
            auxiliar.append(k)
    auxiliar.sort()
    principal.append(auxiliar[:])
    auxiliar.clear()
print('-='*20)
sleep(1)
print(f'{"Mega Sena":^40}')
print('-='*20)
print('  '*5,f'Sorteando {n} jogos','  '*5)
for k in range(0,n):
    print(f'Jogo {k+1} - {principal[k]} ')
    sleep(1)
print('-='*20)