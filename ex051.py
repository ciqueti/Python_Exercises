#Exercício Python 51: Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão.
print('-='*6)
a1 = int(input('Primeiro termo da P.A: '))
k = int(input('Razão da P.A: '))
for i in range (0,10):
    print('A{} = {} '.format(i+1,a1 + i*k), end=' ')