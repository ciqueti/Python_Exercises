#Exercício Python 42: Refaça o DESAFIO 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado: equiláter, isósceles ou escaleno
#Exercício Python 35: Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.
m1 = float(input('Medida 1: '))
m2 = float(input('Medida 2: '))
m3 = float(input('Medida 3: '))
if (m1 < m2 + m3) and (m2 < m1 + m3) and (m3 < m1 + m2):
    print('As medidas formam um triangulo')
    if (m1 == m2 and m2 == m3):
        print('Temos um triangulo Equilátero')
    elif (m1 == m2 or m1 == m3 or m2 == m3):
        print('Temos um Triangulo Isósceles')
    else:
        print('Temos um Triangulo Escaleno')
else:
    print('As medidas não formam um triangulo')