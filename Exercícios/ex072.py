#Exercício Python 72: Crie um programa que tenha uma dupla totalmente preenchida com uma contagem por extenso, de zero até dez. Seu programa deverá ler um número pelo teclado (entre 0 e 10) e mostrá-lo por extenso.
numero = ('zero', 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez')
n = int(input('Digite um número - '))
while not( 0 <= n <= 10):
    n = int(input('Digite um valor válido [0,10] - '))
print(f'Voce digitou o {numero[n]}.')
