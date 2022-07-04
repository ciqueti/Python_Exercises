#Exercício Python 086: Crie um programa que declare uma matriz de dimensão 3x3 e preencha com valores lidos pelo teclado. No final, mostre a matriz na tela, com a formatação correta.
matriz = [[], [], []]
for j in range(0,3):
    for k in range(0,3):
        matriz[j].append(int(input(f'Valor {j}x{k} - ')))
print('=-='*10)
for j in range(0,3):
    for k in range(0,3):
        print(f'[ {matriz[j][k]:^3} ]' , end=' ')
    print()
#for k in range(0,3):
#    print(f'{matriz[k]}')
print('=-='*10)