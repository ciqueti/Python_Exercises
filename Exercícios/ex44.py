#Exercício Python 44: Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
print(('==='*6),'Loja Chiqueti',('==='*6))
p = float(input('Preço das compras: R$'))
print('[1] - à vista dinheiro/cheque: 10% de desconto \n[2] - à vista no cartão: 5% de desconto \n[3] - em até 2x no cartão: preço formal \n[4] - 3x ou mais no cartão: 20% de juros')
n = int(input('Selecione o método de pagamento: '))
if(n == 1):
    print('Sua compra de R${} custará R${:.2f}'.format(p,0.9*p))
elif(n==2):
    print('Sua compra de R${} custará R${:.2f}'.format(p,0.95*p))
elif(n==3):
    print('Compra de R${} parcelada em 2x no valor de R${:.2f}'.format(p,p/2))
elif(n==4):
    m = int(input('Quantas vezes deseja parcerlar? '))
    print('Compra de R${} parcelada em {}x no valor de R${:.2f}'.format(p,m,p*1.2))
print('==='*20)