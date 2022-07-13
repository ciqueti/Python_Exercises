#Aula Funções
def lin(msg):  #Definindo a Função
    print('-'*20)
    print(f'{msg:^20}')
def soma(a,b): #Função com vários Parâmetros
    print(f'A = {a} e B = {b}')
    s = a+b
    print(f'A Soma A + B = {s}')
    print()

def cont(*num): #Se não soubermos quantidade exata de parâmetros? Empacotamento e Desempacotamento
    print(f'Temos ao todo {len(num)} número(s) contado(s). São ele(s):')
    for i in num:
        print(f'{i} -> ', end='')
    print('FIM..')
    print()

def dobra(lst): #Lista como Referência
    cont = 0
    while cont < len(lst):
        lst[cont] *= 2
        cont += 1

#Programa Principal
lin('FUNÇÕES')

lin('SOMA')
soma(4,3)
soma(a=5,b=1)
soma(b=6,a=2)
lin('PARÂMETROS')
cont(8, 2, -6, 9)
cont(1, 2, 3)
cont(7)
valores = [4,5,2,0,3,-2]
lin('DOBRA LISTA') 
print(valores)
dobra(valores)
print(valores)
