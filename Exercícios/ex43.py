#Exercício Python 43: Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu Índice de Massa Corporal (IMC) e mostre seu status, de acordo com a tabela abaixo:
h = float(input('Altura: '))
p = float(input('Peso: '))
imc = p/h**2
print('Seu IMC é {:.2f}'.format(imc))
if (imc < 18.5):
    print('Abaixo do Peso')
elif (18.5 <= imc <= 25):
    print('Peso Ideal')
elif (25 <= imc <= 30):
    print('Sobrepeso')
elif (30 <= imc <= 40):
    print('Obesidade')
else:
    print('Obesidade Mórbida')
