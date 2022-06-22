#Exercício Python 070: Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre: A) qual é o total gasto na compra. B) quantos produtos custam mais de R$1000. C) qual é o nome do produto mais barato. 
print('-='*5, 'Loja Chiqueti', '-='*5)
a = 0
b = 0
c = ''
cont = 0
while True:
    n = str(input('Nome do produto - '))
    p = float(input('Valor - R$'))
    a += p
    cont += 1
    if(cont == 1):
        barato = p
    if (p > 1000):
        b += 1
    if (p <= barato):
        barato = p
        c = n
    dec = ' '
    while dec not in 'SNsn':
        dec = str(input('Comprar Mais? [ S / N ] - ')).upper().strip()[0]
    if dec == 'N':
        break
print(f'A) Total gasto na compra - {a}')
print(f'B) # produtos custam mais de R$1000 - {b}')
print(f'C) Nome do produto mais barato - {c}')
