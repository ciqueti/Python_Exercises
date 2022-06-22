#Exercício Python 36: Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
#Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar. A prestação mensal não pode exceder 30% do 
#salário ou então o empréstimo será negado.
print('\33[33m'+'-##-'*20+'\33[m')
casa = float(input('Valor da Motorhouse? R$ '))
salario = float(input('Salario? R$ '))
anos = int(input('Quantos anos de parcela? '))
prestacao = casa/(12*anos)
print('A prestacao sera de {:.2f}'.format(prestacao))
if (prestacao > 0.3*salario):
    print('EMPRESTIMO NEGADO')
    print('Salario - {} \nPrestacao - {:.2f} \nMeses - {}'.format(salario,prestacao,12*anos))
else:
    print('Emprestimo Concedido')
    print('Salario - {} \nPrestacao - {:.2f} \nMeses - {}'.format(salario,prestacao,12*anos))
print('\33[33m'+'-##-'*20+'\33[m')