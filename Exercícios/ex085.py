#Exercício Python 085: Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única que mantenha separados os valores pares e ímpares. No final, mostre os valores pares e ímpares em ordem crescente.
num = [[] ,[]]
for i in range(0,7):
    n = int(input('Digite um número - '))
    if n % 2 == 0:
        num[0].append(n)
    elif n % 2 == 1:
        num[1].append(n)
num[0].sort()
num[1].sort()
print('-=-'*10)
print(f'Valores Pares - {num[0]}')
print(f'Valores Ímpares - {num[1]}')
print('-=-'*10)