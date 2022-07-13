#Exercício Python 102: Crie um programa que tenha uma função fatorial() que receba dois parâmetros: o primeiro que indique o número a calcular e outro chamado show, que será um valor lógico (opcional) indicando se será mostrado ou não na tela o processo de cálculo do fatorial.
def fatorial(n,show = False):
    """
    Função fatorial, calcula o fatorial de n
    n - Número inteiro
    show - Pârametro opcional - mmostrar ou não a conta realizada
    return - Valor do fatorial
    """
    s = 1
    print(f'{n}! =',end=' ')
    while n != 1:
        if show == True:
            print(f'{n} x',end=' ')
        s *= n
        n -= 1
    if show == True:
        print('1 = ',end='')
    print(s)
    return s

fatorial(5,True)   
help(fatorial) 
