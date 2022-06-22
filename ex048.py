#Exercício Python 48: Faça um programa que calcule a soma entre todos os números que são múltiplos de três e impares que se encontram no intervalo de 1 até 500.
s = 0
cont = 0
for i in range(1,501,2):
    if(i % 3 == 0):
        s += i
        cont += 1
print ('A soma dos {} valores é {}'.format(cont,s))