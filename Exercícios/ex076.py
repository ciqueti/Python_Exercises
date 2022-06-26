#Exercício Python 076: Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência. No final, mostre uma listagem de preços, organizando os dados em forma tabular.
#Exercício sobre formatação

n = ('Arroz', 1.60, 'Frango', 12.50,'Batata', 3.60,'Abóbora', 2.80,'Caneta',1.50, 'Peixe',9.90,'Abacate',7.80,'Cereja', 10,'Uva',5.60)
print('-='*15)
print(f'{"Tabela de Preços":^30}')
print('-='*15)
for i in range (0,len(n),2):
#    print(n[i],end='')
#    print('.'*(20-len(n[i])), end=' R$ ')
#    print(f'{n[i+1]:.2f}')
    print(f'{n[i]:.<20}','R$' ,f'{n[i+1]:>5.2f}')
print('-='*15)

