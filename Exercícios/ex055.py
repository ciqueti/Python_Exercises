#Exercício Python 55: Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.
print('-='*15)
for i in range (1,6,1):
    peso = float(input('Digite o peso da {}ª - '.format(i)))
    if (i == 1):
        maior = peso
        menor = peso
    if (peso > maior):
        maior = peso
    if (peso < menor):
        menor = peso
print('Maior peso - {}kg'.format(maior))
print('Menor peso - {}kg\n'.format(menor))
print('-='*15)

