#Exercício Python 081: Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre:
#A) Quantos números foram digitados.                                                                                                                    #B) A lista de valores, ordenada de forma decrescente.                                                                                          
#C) Se o valor 5 foi digitado e está ou não na lista.
lista = list()
while True:
    lista.append(int(input('Digite um valor - ')))
    n = str(input('Quer continuar [S \ N] - ')).upper().strip()[0]
    if n in 'N':
        break
lista.sort(reverse=True)
print(f'Fora digitados {len(lista)} números')
print(f'Lista decrescente - {lista}')
if 5 in lista:
    print('O valor 5 está na lista.')
else:
    print('O valor 5 não está na lista.')