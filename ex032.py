# Faça um programa que leia um ano qualquer e mostre se ele é bissexto.
import datetime
print('---'*20)
ano = int(input('Digite um ano do Calendário Gregoriano para descobrir se ele é BIssexto (Coloque 0 caso deseje o ano atual): '))
if (ano == 0):
    ano = datetime.date.today().year
if (ano % 4 == 0) and (ano % 100 != 0) or (ano % 400 == 0):
    print('O ano {} É BISSEXTO'.format(ano))
else:
    print('O ano {} NÃO É BISSEXTO'.format(ano))
'''if(ano % 400 == 0):
    print('{} é um ano bissexto'.format(ano))
    quit()
if(ano % 100 == 0):
    print('{} não é um ano bissexto'.format(ano))
    quit()
if(ano % 4 == 0):
    print('{} é um ano bissexto'.format(ano))
    quit()'''
print('---'*20)
