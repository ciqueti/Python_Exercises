#Exercício Python 078: Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.
lista = []
maior_posicao = []
menor_posicao = []
print('--'*10)
for n in range(0,5):
    lista.append(int(input(f'Digite um valor para posição {n} - ')))
print(f'Os valores são - {lista}')
#for i in range (0,len(lista)):
#    if lista[i] == max(lista):
#        maior_posicao.append(i)
#    elif lista[i] == min(lista):
#        menor_posicao.append(i)
#print(f'O maior valor digitado foi o {max(lista)} que está nas posições {maior_posicao}')
#print(f'O menor valor digitado foi o {min(lista)} que está na posições {menor_posicao}')

print(f'O maior valor digitado foi o {max(lista)} que está nas posições - ',end='')
for p, v in enumerate(lista):
    if v == max(lista):
        print(f'{p}', end='..')
print(f'\nO menor valor digitado foi o {min(lista)} que está na posições - ', end='')
for p,v in enumerate(lista):
   if v == min(lista):
       print(f'{p}', end='..')
print()
print('--'*10)

