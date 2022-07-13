#Exercício Python 100: Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar(). A primeira função vai sortear 5 números e vai colocá-los dentro da lista e a segunda função vai mostrar a soma entre todos os valores pares sorteados pela função anterior.
import numbers
from random import randint
from time import sleep


def sorteia(numeros):
    print('-'*15)
    print('NÚMEROS SORTEADOS')
    for i in range(0,5):
        numeros.append(randint(0,20))
        print(f'{numeros[i]} ',end=' -> ')
        sleep(0.3)
    print('FIM')

def somapar(lst):
    print('-'*15)
    tot = 0
    for i in lst:
        if i % 2 == 0:
            tot +=i
    print(f'Soma de Pares = {tot}')

num = []
sorteia(num)
somapar(num)