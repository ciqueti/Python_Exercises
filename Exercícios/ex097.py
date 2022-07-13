#Exercício Python 097: Faça um programa que tenha uma função chamada escreva(), que receba um texto qualquer como parâmetro e mostre uma mensagem com tamanho adaptável.
def titulo(msg):
    print('='*(len(msg)+6))
    print(f'   {msg}')
    print('='*(len(msg)+6))


mensagem = 'CENTRALIZAÇÃO'
titulo(mensagem)
mensagem = 'CURTO'
titulo(mensagem)
mensagem = 'PALAVRA LONGA E DE EFEITO'
titulo(mensagem)