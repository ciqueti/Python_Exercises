#Exercício Python 33: Faça um programa que leia três números e mostre qual é o maior e qual é o menor.
n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
n3 = int(input('Terceiro valor: '))
if (n1 <= n2):
    a = n1
    b = n2
else:
    a = n2
    b = n1
if (a >= n3):
    a = n3
if(b <= n3):
    b = n3
print('Menor valor: {} \nMaior Valor: {}'.format(a,b))