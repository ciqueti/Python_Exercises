#Crie um programa que leia o nome completo de uma pessoa e mostre
nome = str(input('Digite seu nome completo: ')).strip()
print('Seu nome maiúsculo é {}'.format(nome.upper()))
print('Seu nome minúsculo é {}'.format(nome.lower()))
lista = nome.split()
letras = len(nome) - nome.count(' ')
print('Seu nome {} possui {} letras'.format(nome,letras))
print('Seu primeiro nome tem {} letras'.format(nome.find(' ')))
print('Seu primeiro nome {} possui {} letras'.format(lista[0], len(lista[0])))