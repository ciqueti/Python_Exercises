#Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.
p = float(input('Digite o preco do produto: '))
novo = p*0.95
print('O valor do produto com 5% de desconto será de: {:.2f}'.format(novo))