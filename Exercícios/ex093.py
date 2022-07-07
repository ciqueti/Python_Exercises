#Exercício Python 093: Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador e quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida. No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.
#ficha = {'nome':'',  [part1,part2], total gols}
ficha = {}
ficha['nome'] = input('Nome do Jogador: ')
ficha['partidas'] = list()
n = int(input('Total de Partidas: '))
ficha['total gols'] = 0
for i in range(0,n):
    ficha['partidas'].append(int(input(f'Gols da {i+1}o. partida: '))) 
    #ficha['total gols'] += ficha['partidas'][i]
ficha['total gols'] = sum(ficha['partidas']) 
print('=-'*10)
print(ficha)
print('=-'*10)
for k,v in ficha.items():
    print(f'{k} - {v}')
print('=-'*10)
print(f'O jogador {ficha["nome"]} jogou {n} partidas e fez {ficha["total gols"]} gols')
for k,v in enumerate(ficha['partidas']):
    print(f'     => Partida {k+1} - {v} Gols')
print(f'Foi um total de {ficha["total gols"]} Gols!')
print('=-'*10)