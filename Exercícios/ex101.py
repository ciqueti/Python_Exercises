#Exercício Python 101: Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento de uma pessoa, retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL e OBRIGATÓRIO nas eleições.
from datetime import datetime
def voto(ano):
    ano = datetime.today().year - ano
    print(f'Usuário com {ano} anos de Idade')
    if ano < 16:
        sit = 'NEGADO'
    elif ano >= 16 and ano < 18:
        sit = 'OPCIONAL'
    elif ano < 60:
        sit = 'OBRIGATÓRIO'
    elif ano >= 60:
        sit = 'OPCIONAL'
    return sit

n = int(input('Ano de nascimento: '))
situa = voto(n)
print(f'Situação Voto - {situa}')