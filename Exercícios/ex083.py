#Exercício Python 083: Crie um programa onde o usuário digite uma expressão qualquer que use parênteses. Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta.
exp = list(str(input('Digite uma expressão - ')))
cont = 0
for i in exp:
    if i == '(':
        cont +=1
    elif i == ')':
        cont -= 1
if cont == 0:
    print('Expressão Válida')
elif cont:
    print('Expressão Inválida')
    