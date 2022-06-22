import datetime
idade = int(input('Ano de nascimento: '))
ano = datetime.date.today().year
print('Quem nasceu em {} possui {} anos em {}'.format(idade,ano-idade,ano))
if(ano-idade < 17):
    print('Nao ha necessidade de se alistar, ainda faltam {} anos'.format(17 + idade - ano))
elif(ano-idade > 17):
    print('Tempo de alistamento expirado, voce deveria ter se alistado ha {} anos'.format(ano-idade - 17))
else:
    print('Voce pode se alistar')
print('')