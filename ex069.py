#Exercício Python 069: Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre: A) quantas pessoas tem mais de 18 anos. B) quantos homens foram cadastrados.C) quantas mulheres tem menos de 20 anos.
a = 0
b = 0
c = 0
while True:
    print('-='*5,'Cadastre uma Pessoa','-='*5)
    n = int(input('Idade - '))
    s = str(input('Sexo [ M / F ] - ')).upper().strip()[0]
    if (n > 18):
        a += 1
    if (s == 'M'):
        b +=1
    if (s == 'F' and n < 20):
        c +=1
    flag = str(input('Deseja cadastrar mais uma pessoa [ S / N ] - ')).upper().strip()[0]
    if flag == 'N':
        break
print (f'A) quantas pessoas tem mais de 18 anos - {a}')
print(f'B) quantos homens foram cadastrados - {b}')
print(f'C) quantas mulheres tem menos de 20 anos. - {c}')



