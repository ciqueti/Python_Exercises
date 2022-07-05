#Exercício Python 090: Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário. No final, mostre o conteúdo da estrutura na tela.
ficha = dict()
ficha['Nome'] = str(input('Nome do Aluno - '))
ficha['Média'] = float(input('Média do Aluno - '))
if ficha['Média'] < 4:
    ficha['Situação'] = 'Reprovado'
elif ficha['Média'] < 6:
    ficha['Situação'] = 'Recuperação'
else:
    ficha['Situação'] = 'Aprovado'
print('=='*25)
for k,v in ficha.items():
    print(f'| {k} - {v}',end=' ')
print()
print('=='*25)