#Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.
nome = str(input('Digite seu nome completo: ')).strip()
lista = nome.split()
print('Seu primeiro nome é {} \nSeu último nome é {}'.format(lista[0], lista[len(lista)-1]))