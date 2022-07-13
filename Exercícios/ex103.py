#Exercício Python 103: Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros opcionais: o nome de um jogador e quantos gols ele marcou. O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum dado não tenha sido informado corretamente.
def ficha(nome='<desconhecido>',gols=0):
    if nome == '':
        nome = '<desconhecido>'
    
    print(f'O jogador {nome} fez {gols} gol(s)')

m = str(input('Nome do jogador - ')).strip()
fg = (input('Gols feitos - '))
if fg.isnumeric() == True:
    fg = int(fg)
else:
    fg = int(0)
ficha(m,fg)