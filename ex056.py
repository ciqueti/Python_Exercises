#Exercício Python 56: Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre: a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.
media = 0
contMulher = 0
maiorIdadeM = 0
for i in range (1,5,1):  #Coletando dados
    print('\n---- {}ª Pessoa ----'.format(i))
    nome = str(input('Nome - '))
    idade = int(input('Idade - '))
    sexo = str(input('Sexo [M/F] - ')).upper()

    media += idade/4 #Tratando dados
    if (sexo == 'F' and idade < 20):
        contMulher += 1
    if (sexo == 'M' and idade > maiorIdadeM):
        maiorIdadeM = idade
        nomeM = nome    
print('-='*15) #Exibindo dados
print('Média de idade - {} anos'.format(media))
print('Homem mais velho - {}'.format(nomeM))
print('#Mulheres com menos de 20 anos - {} mulheres'.format(contMulher))
print('-='*15)