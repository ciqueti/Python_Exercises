#O mesmo professor do desafio 19 quer sortear a ordem de apresentação de trabalhos dos alunos. Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.
import random
a1 = input('Primeira Aluna: ')
a2 = input('Segunda aluna: ')
a3 = input('Terceira Aluna: ')
a4 = input('Quarta Aluna: ')
lista = [a1,a2,a3,a4]
random.shuffle(lista)
print('Ordem de Apresentacão: ', lista)
