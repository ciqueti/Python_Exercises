#Exercício Python 52: Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.
p = int(input('Digite um número inteiro: '))
bol = True
for i in range (2,p):
    if (p % i == 0):
        bol = False
if(bol):
    print('{} é primo!'.format(p))
else:
    print('{} não é primo!'.format(p))