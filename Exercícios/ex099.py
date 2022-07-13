#Exercício Python 099: Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros. Seu programa tem que analisar todos os valores e dizer qual deles é o maior.
def maior(*n):
    print('=='*15)
    if len(n) == 0:
        print('Foi informado 0 valor. Maior valor é 0.')
    else:
        for i in n:
            print(f'{i}', end=' ')
        print(f'| Foram informados {len(n)} valores')
        print(f'O maior valor é {max(n)}')
        


maior(1,2,3,4,5)
maior(3,6,-2,-7,2345)
maior(3)