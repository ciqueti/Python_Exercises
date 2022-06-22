#Exercício Python 57: Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores ‘M’ ou ‘F’. Caso esteja errado, peça a digitação novamente até ter um valor correto.
n = input('Informe seu sexo [M/F] - ').upper().strip()[0]
while n not in 'MF':
    n = str(input('Inválido. Informe seu sexo [M/F] - ')).strip().upper()[0]    
print('Sexo {} registrado com sucesso.'.format(n))