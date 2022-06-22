#Exercício Python 071: Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues. OBS:considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.
from math import trunc


print('-='*5, 'Caixa','-='*5)
n = float(input('Dinheiro a ser sacado - R$')).__trunc__()
p50 = (n/50).__trunc__()
n -= p50*50
print(f'{p50} nota(s) de R$ 50.00') 
p20 = (n/20).__trunc__()
n -= p20*20
print(f'{p20} nota(s) de R$ 20.00')
p10 = (n/10).__trunc__()
n -= p10*10
print(f'{p10} nota(s) de R$ 10.00')
print(f'{n} nota(s) de R$ 1.00')
print('-='*5,'Volte Sempre','-='*5)