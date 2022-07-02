#Exercício Python 082: Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente. Ao final, mostre o conteúdo das três listas geradas.
lista = list()
lista_par = list()
lista_impar = list()
while True:
    lista.append(int(input('Digite um número - ')))
    opc = str(input('Adicionar mais um valor [S \ N] - ')).upper().strip()[0]
    if opc in 'N':
        break
for i in lista:
    if i%2 == 0:
        lista_par.append(i)
    else:
        lista_impar.append(i)
print(f'Lista Gerada - {lista}')
print(f'Lista de Pares - {lista_par}')
print(f'Lista Ímpares - {lista_impar}')