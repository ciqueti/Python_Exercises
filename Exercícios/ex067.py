#Exercício Python 67: Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário. O programa será interrompido quando o número solicitado for negativo.
while True:
    n = int(input('Digite um valor [Negativo para Encerramento] - '))
    if n < 0:
        break
    for i in range (1,11,1):
        print(f' {n:2} X {i:2} = {n*i:2}')
    