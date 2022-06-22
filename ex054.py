#Exercício Python 54: Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.
import datetime
ano = datetime.date.today().year
velho = 0
novo = 0
for i in range (1,8,1):
    n = int(input('Ano de nascimento da {}ª pessoa: '.format(i)))
    if (ano - n < 18):
        novo += 1
    else:
        velho +=1
print('Pessoas Maior de idade: {}'.format(velho))
print('Pessoas Menores de idade: {}'.format(novo))
    
