#Exercício Python 096: Faça um programa que tenha uma função chamada área(), que receba as dimensões de um terreno retangular (largura e comprimento) e mostre a área do terreno.
from time import sleep
def area(alt,lar):
    print('=='*15)
    print(f'Altura: {alt}m  Largura: {lar}m')
    are = alt*lar
    print(f'Área: {are}m2')
    print('=='*15)


n1 = float(input('Altura do Terreno(m): '))
n2 = float(input('Largura do Terreno(m): '))
print('Calculando área..')
sleep(1)
area(n1,n2)