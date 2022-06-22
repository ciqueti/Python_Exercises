#Exercício Python 038: Escreva um programa que leia dois números inteiros e compare-os. mostrando na tela uma mensagem:
n1 = int(input(' Primeiro valor: '))
n2 = int(input(' Segundo valor: '))
if(n1 > n2):
    print(' Maior valor: \33[35m {} \33[m \n Menor valor: \33[35m {} \33[m'.format(n1,n2))
elif(n2 > n1):
    print(' Maior valor: \33[32m {} \33[m \n Menor valor: \33[32m {} \33[m'.format(n2,n1))
else:
    print('Os valores sao os mesmos: \33[33m {} \33[m'.format(n1))