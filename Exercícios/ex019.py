#Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome dos alunos e escrevendo na tela o nome do escolhido.
#import random
from random import choice
a1 = input('Digite o nome do aluno1: ')
a2 = input('Digite o nome do aluno2: ')
a3 = input('Digite o nome do aluno3: ')
a4 = input('Digite o nome do aluno4: ')
lista = [a1,a2,a3,a4]
escolhido = choice(lista)
print('Vocë deverá apagar a lousa: {}'.format(escolhido))
