#Exercício Python 098: Faça um programa que tenha uma função chamada contador(), que receba três parâmetros: início, fim e passo. Seu programa tem que realizar três contagens através da função criada:
from time import sleep
def contador(ini,fim,passo):
    print('=='*15)
    print(f'Contagem de {ini} até {fim} com passo {passo}')
    if fim > ini:
        for i in range(ini,fim+1,passo):
            print(i, end=' => ')
            sleep(0.3)
    elif fim < ini:
        for i in range(ini,fim-1,passo):
            print(i, end=' => ')
            sleep(0.3)
    print('FIM')
print('Agora é sua vez de personalizar a contagem')
contador(1,10,1)
contador(10,0,-2)
i = int(input('Começo: '))
f = int(input('Fim: '))
p = int(input('Passo: '))
contador(i,f,p)
