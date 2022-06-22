#A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um 
# atleta e mostre sua categoria, de acordo com a idade:
n = int(input('Ano de Nascimento: '))
if (n <= 9):
    print('Nadador Mirim')
elif(n <= 19):
    print('Nadador Junior')
elif(n <= 25):
    print('Nadador Senior')
else:
    print('Nadador Master')