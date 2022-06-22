#Exercício Python 50: Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o.
print('-+-'*10,'SOMA DOS PARES','-+-'*10)
s = 0
cont = 0
for i in range (1,7):
    n = int(input('Digite um número inteiro: '))
    if (n % 2 == 0):
        s += n
        cont += 1
print('Voce informou {} valores pares, A soma é {}!'.format(cont,s))