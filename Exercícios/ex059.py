#Exercício Python 059: Crie um programa que leia dois valores e mostre um menu na tela:[ 1 ] somar [ 2 ] multiplicar [ 3 ] maior [ 4 ] novos números[ 5 ] sair do programa Seu programa deverá realizar a operação solicitada em cada caso.
from time import sleep
op = -1
n1 = int(input('Primeiro valor - '))
n2 = int(input('Segundo valor - '))
while op !=5:
    print('=='*10)
    print('[ 1 ] somar \n[ 2 ] multiplicar \n[ 3 ] maior \n[ 4 ] novos números \n[ 5 ] sair do programa')
    op = int(input('Opção - '))
    print('=='*10)
    while op not in [1,2,3,4,5]:
        op = int(input('Inválido. Opção - '))
    if (op == 1):
        print('Operador Soma - {} + {} = {}'.format(n1,n2,n1+n2))
    elif (op==2):
        print('Operador Multiplicação - {} x {} = {}'.format(n1,n2,n1*n2))
    elif (op==3):
        if (n1 > n2):
            print('{} Maior - {} Menor'.format(n1,n2))
        elif (n1 < n2):
            print('{} Maior - {} Menor'.format(n2,n1))
        else:
            print('São os mesmos valores')
    elif (op == 4):
        n1 = int(input('Primeiro valor - '))
        n2 = int(input('Segundo valor - '))
    sleep(2)
print('Finalizando..',end='')
sleep(1)
print('...',end='')
sleep(1)
print('..')
print('Fim')