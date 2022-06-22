#Exercício Python 65: Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.
n = int(input('Digite um número: '))
media = n
cont = 1
maior = menor =n
r = str(input('Deseja continuar? [ S / N ] - ')).strip().upper()
while(r !='N'):
    n = int(input('Digite um número: '))
    cont +=1
    media +=n
    if maior < n:
        maior = n
    if menor > n:
        menor = n
    r = str(input('Deseja continuar? [ S / N ] - ')).strip().upper()
print('Média - {:.2f} \nMaior - {} \nMenor - {} \n# valores - {}'.format(media/cont,maior,menor,cont))