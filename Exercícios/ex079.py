#Exercício Python 079: Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. Caso o número já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos digitados, em ordem crescente.
lista = []
while True:
    v = (int(input('Digite um valor - ')))
    if v in lista:
        print('Valor já existente, não cadastrado')
    else:
        lista.append(v)
        print('Adicionado com sucesso')
    n = input('Continuar [ S \ N ] - ').upper().strip()[0]
    if n == 'N':
        break
print('==' *15)
print(f'Lista digitada - {lista}')
print(f'Lista digitada ordenada - {sorted(lista)}')
