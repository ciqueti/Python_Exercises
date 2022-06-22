#Exercício Python 34: Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
#Para salários superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.
salario = float(input('Digite seu salario: '))
if (salario > 1250):
    salario = 1.1*salario
else:
    salario = 1.5*salario
print('Seu novo salario - R$ {:.2f}'.format(salario))
