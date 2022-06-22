#Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite.
print('-=-'*20)
v = float(input('Digite a velocidade que está dirigindo: '))
if v <= 80 :
    print('Velocidade Segura, siga em Paz')
else:
    multa = 7*(v-80)
    print('MULTADO! As vezes vocë precisa dar uma de louco, dessa vez custou R${:.2f}'.format(multa))
print('Tenha uma Boa Viagem!')
print('-=-'*20)