#Exercício Python 089: Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta. No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente.
auxiliar = []
boletim = list()
while True:
    auxiliar.append(str(input('Nome - ')))                                      # nome = input()
    auxiliar.append(float(input('Nota 1 - ')))                                  # n1 = input()
    auxiliar.append(float(input('Nota 2 - ')))                                  # n2 = input()
    auxiliar.append(((auxiliar[1]+auxiliar[2])/2))                              # media = input()
    opc = str(input('Deseja Continuar [ S \ N ] - ')).upper().strip()[0]        # boletim.append([nome,[n1,n2],media])
    boletim.append(auxiliar[:])
    auxiliar.clear()
    if opc in 'N':
        break
print('=='*20)
print('No.       Nome                Média')
print('=='*20)
for i, c in enumerate(boletim):
    print(f'{i}         {c[0]:<20} {c[3]:.2f} ')
print('=='*20)
while True:
    k = int(input('Digite No. para ver as notas [999 encerra]: '))
    if k == 999:
        break
    print(f'No.{k}   Nome: {boletim[k][0]}  Nota 1 - {boletim[k][1]} Nota 2 - {boletim[k][2]}   Média: {boletim[k][3]:.2f}')
    print('-='*10)

