#Exercício Python 58: Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.
import random
n = random.randint(0,10)
print('-='*10)
print('Pensei em um número no intervalo [0,10].')
r = int(input('Qual sua tentativa? '))
cont = 1
while (r!=n):  #while not 'False' - Ficará no loop até ser True
    if r < n:
        print('Mais..', end=' ')
    else:
        print('Menos..', end=' ')
    r = int(input('Resposta errada, tente novamente: '))
    cont +=1    
print('Parabéns! SCORE: {} tentativas'.format(cont))
print('-='*10)