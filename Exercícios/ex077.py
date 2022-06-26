#Exercício Python 077: Crie um programa que tenha uma tupla com várias palavras (não usar acentos). Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.
print('-='*15)
tupla = ('AbAcAtE', 'batata', 'tgb','extensao','maça','rubi','esmeralda','pirata')
for elemento in tupla:
    print(f'Na palavra {elemento.upper()} temos - ',end='') 
    for letra in elemento:
        if letra.lower() in 'aeiou':
            print(f'{letra.lower()}', end=' ')
    print('')
print('-='*15)
