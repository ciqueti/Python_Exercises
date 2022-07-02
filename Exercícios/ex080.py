#Exercício Python 080: Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista, já na posição correta de inserção (sem usar o sort()). No final, mostre a lista ordenada na tela.
lista = []
n  = int(input('Digite um número - '))
print('Valor adicionado no fim da lista')
lista.append(n)
for i in range(0,5):
  n  = int(input('Digite um número - '))
  if n <= min(lista):
    lista.insert(0,n)
    print(f'Valor {n} Adicionado na posição 0')  
  elif n >= max(lista):
    lista.append(n)
    print(f'Valor {n} Adicionado no fim da lista')
  else:
    cont = 0
    while n >= lista[cont]:
      cont += 1
    lista.insert(cont,n)
    print(f'Valor {n} adicionado na posição {cont}')
print(f'Lista na ordem Correta - {lista}')