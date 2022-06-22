#Exercício Python 13: Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.
salario = float(input('Digite o seu salário: R$ '))
aumento = float(input('Digite a porcentagem do aumento (de zero a um): '))
novo = salario*(1+aumento)
print('Seu salário: R$ {} \nSeu aumento: {}% \nSeu novo salário: R$ {:.2f}'.format(salario,100*aumento,novo))
