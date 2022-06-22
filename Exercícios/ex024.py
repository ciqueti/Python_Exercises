#Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome “SANTO”.
nome = str(input('Digite o nome da cidade: '))
nome = nome.strip()
nome = nome.lower()
lista = nome.split()
print('antonio' in lista[0] )
print(nome[:7] == 'antonio')
print(nome[:7])