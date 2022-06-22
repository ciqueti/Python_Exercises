# Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:
n1 = float(input('Nota 1 - '))
n2 = float(input('Nota 2 - '))
media = (n1 + n2)/2
print('Tirando {} e {} sua media sera - {}'.format(n1,n2,media))
if (media < 5):
    print('REPROVADO!!')
elif (media < 6.9):
    print('RECUPERACAO!!')
else:
    print('APROVADO!!')