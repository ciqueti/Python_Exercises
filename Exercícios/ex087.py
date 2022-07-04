#Exercício Python 087: Aprimore o desafio anterior, mostrando no final: 
#A) A soma de todos os valores pares digitados.
#B) A soma dos valores da terceira coluna.
#C) O maior valor da segunda linha.
matriz = [[0,0,0],[0,0,0],[0,0,0]]
soma_par = 0
soma_col3 = 0
maior_lin2 = list()
for l in range(0,3):
    for c in range(0,3):
        matriz[l][c] = int(input(f'Valor [{l}][{c}] - '))
        if matriz[l][c] % 2 == 0:
            soma_par += matriz[l][c]
        if c == 2:
            soma_col3 += matriz[l][c]
        if l == 1:
            maior_lin2.append(matriz[1][c])
print('-=-'*10)
for l in range(0,3):
    for c in range(0,3):
        print(f'[{matriz[l][c]:^5}]', end=' ')
    print()
print('-=-'*10)
print(f'Soma dos Pares - {soma_par}')
print(f'Soma coluna 3 - {soma_col3}')
print(f'Máximo linha 2 - {max(matriz[1])}')
