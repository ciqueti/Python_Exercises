#Exercício Python 63: Escreva um programa que leia um número N inteiro qualquer e mostre na tela os N primeiros elementos de uma Sequência de Fibonacci. 
from re import A


n = int(input('Quantos termos deseja? '))
cont = 0
a = 0
b = 1
print('0 -> 1 ->',end=' ')
while(cont != n - 2):
    c = b + a
    print('{} ->'.format(c), end=' ')
    cont +=1
    a = b
    b = c
print('FIM')
    
