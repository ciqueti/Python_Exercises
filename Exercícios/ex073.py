#Exercício Python 073: Crie uma tupla preenchida com os 10 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:
#a) Os 5 primeiros times.
#b) Os últimos 4 colocados.
#c) Times em ordem alfabética. 
#d) Em que posição está o time da Botafogo.

time = ('Palmeiras', 'Corinthinas', 'Atlético-PR', 'Atlético-MG', 'Internacional' ,'Fluminense','Bota-fogo','Santos','São Paulo', 'Bragantino')
print(f'Times do Campeonato Brasileiro -  {time}')
print(f'Os 5 primeiros colocados - {time[:5]}')
print(f'Os últimos 4 colocados - {time[-4:]} ')
print(f'Times em ordem alfabética - {sorted(time)}')
print(f'O Botafogo está na {time.index("Bota-fogo")+1}^Posição') #Aspas duplas usada para devido a interpolação (aspas simples com duplas)
