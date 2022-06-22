#Exercício Python 35: Desenvolva um programa que leia o comprimento 
#de três retas e diga ao usuário se elas podem ou não formar um triângulo.
print('Analisador de Triangulos')
l1 = float(input('Primeiro comprimento: '))
l2 = float(input('Segundo comprimento: '))
l3 = float(input('Terceiro comprimento: '))
if (l1 < l2 + l3) and (l2 < l1 + l3) and (l3 < l1 + l2):
    print('As medidas SIM formam um triangulo')
else:
    print('As medidas NAO formam um triangulo')