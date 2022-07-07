#Exercício Python 092: Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-o (com idade) em um dicionário. Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário. Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar. 30anos contribuição
from datetime import date
from time import sleep
n = date.today().year

ficha = {}
ficha['Nome'] = str(input('Nome - '))
ficha['Ano Nascimento'] = int(input('Ano de Nascimento - '))
ficha['Carteira de Trabalho'] = int(input('CTPS (0 não tem) - '))
ficha['Idade'] = (n - ficha['Ano Nascimento'])
if ficha['Carteira de Trabalho'] != 0:
    ficha['Ano Contratação'] = int(input('Ano de Contratação - '))
    ficha['Sálario'] = int(input('Sálario R$ - '))
    ficha['Contribuição Restante'] = 30 - (n - ficha['Ano Contratação'])
print('=='*15)
for k,v in ficha.items():
    print(f'- {k} tem o valor {v}')
    sleep(0.5)
print('=='*15)