#Exercício Python 53: Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços. Exemplos de palíndromos:
from ntpath import join


print('-='*15)
frase = str(input('Digite uma frase: ')).strip().upper()#.replace(' ','')
fraseNew = frase.split()
fraseNew = ('').join(fraseNew)
print(fraseNew)
inverso = fraseNew[::-1]
'''tamanho = len(fraseNew) - 1
bol = True
for i in range (0, tamanho):
    if (fraseNew[i] != fraseNew[tamanho - i]):
        bol = False'''
if (inverso == fraseNew):
    print('A palavra {} invertida é {}\nTemos um Palíndromo!'.format(fraseNew, inverso))
else:
    print('A palavra {} invertida é {}\nNão temos um Palíndromo!'.format(fraseNew, inverso))
print('-='*15)
    