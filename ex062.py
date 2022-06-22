#Exercício Python 62: Melhore o DESAFIO 61, perguntando para o usuário se ele quer mostrar mais alguns termos. O programa encerrará quando ele disser que quer mostrar 0 termos.
print('Gerador de PA')
n = int(input('Primeiro Termo: '))
k = int(input('Razão da PA: '))
an = n + 9*k
while(n!= an +k):
    print('{} -> '.format(n),end='')
    n = n + k
op = 1
cont = 10
while (op != 0):
    op = int(input('Quantos termos quer ver mais? '))
    an += op*k
    cont += op
    while(n!= an +k):
        print('{} -> '.format(n),end='')
        n = n + k
print('Finalizando PA com {} termos.'.format(cont))