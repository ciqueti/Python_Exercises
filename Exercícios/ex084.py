#Exercício Python 084: Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final mostre:
#A) Quantas pessoas foram cadastradas.
#B) Uma listagem com as pessoas mais pesadas.        
#C) Uma listagem com as pessoas mais leves.
lista = list()
galera = list()
peso = list()
while True:
    lista.append(str(input('Nome - ')))
    lista.append(int(input('Peso - ')))
    peso.append(lista[1])
    galera.append(lista[:])
    lista.clear()
    opc = input('Deseja Continuar [S \ N ] - ').upper().split()[0]
    if opc == 'N':
        break
print('-='*10)
print('Pessoas com maior valor de Peso - ',end='')
for i in galera:
    if i[1] == max(peso):
        print(f'{i[0]}', end='.. ')
print('\nPessoas com menor valor de Peso - ', end='')
for i in galera:
    if i[1] == min(peso):
        print(f'{i[0]} ', end='.. ')
print(f'\n#Pessoas Cadastradas - {len(galera)}')
print('-='*10)
