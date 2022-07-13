#Exercício Python 104: Crie um programa que tenha a função leiaInt(), que vai funcionar de forma semelhante 'a função input() do Python, só que fazendo a validação para aceitar apenas um valor numérico.

def leiaInt():
    while True:
        n = input('Digite um número: ')
        if n.isnumeric() == True:
            n = int(n)
            return(n)
        else:
            print('ERRO. Formato Inválido')


p = leiaInt()
print(f'O número é {p}')