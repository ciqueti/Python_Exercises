#Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.
print('+-+'*20)
n = float(input('Qual a distäncia da sua viagem: '))
if(n <= 200):
    valor = n*0.50
else:
    valor = n*0.45
print('Sua viagem custará R$ {:.2f}'.format(valor))
print('+-+'*20)