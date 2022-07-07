#Exercício Python 095: Aprimore o desafio 93 para que ele funcione com vários jogadores, incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador.
ficha = {}
tabela = list()
while True:
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
    tabela.append(ficha.copy())
    ficha.clear()
    opc = str(input('Deseja Cadastrar mais [S \ N ] - ')).upper().strip()[0]
    while opc not in 'SN':
        opc = input('ERRO. Digite apenas S ou N - ').upper().strip()[0]
    if opc == 'N':
        break
print('-='*17)
print(f'{"Cód":<6}',f'{"gols":<21}',f'{"total":<7}')
print('-='*17)
for i,j in enumerate(tabela):
    print(f'{(i):<6}',f'{str(j["partidas"]):<21}',f'|{(j["total gols"]):<7}')
print('-='*17)
while True:
    opc2 = int(input('Deseja mostrar os dados de qual Jogador? [999 encerrar] - '))
    if opc2 == 999:
        break
    if opc2 >= len(tabela):
        print('ERRO. Código Inválido')
    else:
        for k,v in enumerate(tabela):
            if k == opc2:
                print(f'\nO jogador {v["nome"]} fez {v["total gols"]} gols em {len(v["partidas"])} partidas')
                for c,j in enumerate(v['partidas']):
                    print(f'Jogo {c+1} fez {j} gols')
                print('-='*17)
print('ENCERRANDO..')