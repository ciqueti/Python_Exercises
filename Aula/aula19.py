#Dicionários {}
pessoa = {'nome':'Leonardo Chiqueti', 'idade':'23', 'sexo':'M', 'apagar':'comadando del'}
print(f'O {pessoa["nome"]} tem {pessoa["idade"]} anos')
pessoa['peso'] = 75
print(pessoa['peso'])
print(pessoa.keys())
print(pessoa.values())
print(pessoa.items())
del pessoa['apagar'] #deletando um elemento
for k, v in pessoa.items(): # .keys(),  .values()
    print(f'{k} = {v}')
playlist = []
musica1 = {'Nome':'Feeling Good','Artista':'Gorillaz'}
musica2 = {'Nome':'Before I Forget', 'Artista':'Slipknot'}
playlist.append(musica1)
playlist.append(musica2)
print(playlist[1]['Nome'])

musica = dict()
playlist2 = list()
for i in range(0,2):
    musica['Nome'] = str(input(f'Nome da {i+1}o. Música - '))
    musica['Nota'] = int(input('De 0 a 10 - '))
    playlist2.append(musica.copy()) #Fatiamento não funciona em Dicionários p/ isso temos o método copy()
for faixas in playlist2:
    for v in faixas.values():
        print(f'{v}', end=' | ')
    print()