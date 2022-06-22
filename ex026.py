#Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra “A”, em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.
frase = str(input('Digite sua frase: ')).strip()
frase = frase.lower()
print('Letra A aparece {} vezes'.format(frase.count('a')))
print('Aparece primeiro na posicao {}'.format(frase.find('a')+1))
print('Aparece pela última vez na posicão {}'.format(frase.rfind('a')+1))