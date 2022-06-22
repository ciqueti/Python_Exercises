n = (input('Digite algo: '))
print('O que voce escreveu foi `{}`, claramente uma {}'.format(n, type(n)))
print('Ele é numérico? {}'.format(n.isnumeric()))
print('Ele é alfabético? {}'.format(n.isalpha()))
print('É algum deles? {}'.format(n.isalnum()))
#print('É Decimal? {} '.format(n.isdecimal()))
print('Pode ser impresso? {} '.format(n.isprintable()))

