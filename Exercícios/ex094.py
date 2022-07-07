#Exercício Python 094: Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista. No final, mostre: 
#A) Quantas pessoas foram cadastradas
#B) A média de idade
#C) Uma lista com as mulheres
#D) Uma lista de pessoas com idade acima da média
pessoas = list()
individuo = {}
opc = ''
media = 0
while True:
    individuo['Nome'] = input('Nome: ')
    individuo['Sexo'] = input('Sexo [M / F]: ').upper().strip()[0]
    while (individuo['Sexo'] not in ('MF')):
        individuo['Sexo'] = input('ERRO. Tente novamente[M / F]: ').upper().strip()[0]
    individuo['Idade'] = int(input('Idade: '))
    pessoas.append(individuo.copy())
    individuo.clear()
    opc = str(input('Adicionar Mais [S / N] - ')).upper().strip()[0]
    while opc not in ('SN'):
        opc = input('ERRO. Digite apenas S ou N: ')
    if opc == 'N':
        break
print('-='*15)
print(f'Foram Cadastrados {len(pessoas)} pessoas.')
for i in pessoas:
    media += i['Idade']/len(pessoas)
print(f'A média de idade é {media:.2f}')
print('=='*10,'Mulheres','=='*10)
for i in pessoas:
    if i['Sexo'] == 'F':
        print(f'Nome - {i["Nome"]}') 
print('=='*10,'Indíviduos acima da idade média','=='*10)
for i in pessoas:
    if i['Idade'] > media:
        print(f'Nome - {i["Nome"]}')