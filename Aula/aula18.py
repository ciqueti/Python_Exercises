#Listas Parte 2
#teste = list()
#teste.append('Gus')
#teste.append(40)
#galera = list()
#galera.append(teste[:])
#teste[0] = 'Maria'
#teste[1] = '22'
#galera.append(teste[:])
#print(galera)

#pessoas = [['Joao',16], ['Pedro',5], ['Dante', 40]]
#print(pessoas)
#print(pessoas[0])
#print(pessoas[2][0])
#for p in pessoas:
#    print(f'Nome - {p[0]} Idade - {p[1]}')
maior = menor = 0
dados = list()
galera = list()

for i in range (0,3):
    dados.append(str(input('Nome - ')))
    dados.append(int(input('Idade - ')))
    galera.append(dados[:])
    dados.clear()

for p in galera:
    if p[1] >= 18:
        print(f'{p[0]} é maior de idade')
        maior +=1
    elif p[1] < 18:
        print(f'{p[0]} é menor de idade')
        menor +=1
print(galera)