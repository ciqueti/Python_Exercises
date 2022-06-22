#Exercício Python 49: Refaça o DESAFIO 9, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.
print('-='*15)
n = int(input('Digite um número inteiro: '))
for i in range (1,11):
    print('{} X {:2} = {:2}'.format(n,i,n*i))
print('-='*15)