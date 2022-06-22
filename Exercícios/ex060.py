#Exercício Python 060: Faça um programa que leia um número qualquer e mostre o seu fatorial.
n = int(input('Cálculo fatorial! Digite um número: '))
s=1
if(n >= 1):
    print('{}! = {}'.format(n,n), end=' ')
    while (n!=1):
        s = s*n
        n = n -1    
        print('x {}'.format(n), end=' ')
    print('= {}'.format(s))
elif(n==0):
    print('0! = 1 - por definição')
else:
    print('Digito Inválido')