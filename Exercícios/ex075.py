#Exercício Python 075: Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:
#A) Quantas vezes apareceu o valor 9.
#B) Em que posição foi digitado o primeiro valor 3.
#C) Quais foram os números pares..
n = (int(input('Digite primeiro número - ')),int(input('Digite segundo número - ')),int(input('Digite terceiro número - ')),int(input('Digite o último número - ')))
print(f'Usuário digitou {n}')
print(f'O número 9 aparece {n.count(9)} vezes')
if 3 in n:
    print(f'O número 3 está na posição {n.index(3)+1}')
else:
    print('Número 3 não foi digitado')
print('Números pares ', end='')
for i in n:
    if i%2 == 0:
        print(f'- {i}', end=' ')
