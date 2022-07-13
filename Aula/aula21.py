#help(print)
def contador(i,f,p):
    """       Docstring - Documentação da sua função (ou outra qualquer)
    i -> inicio da contagem
    f -> fim da contagem
    p -> passo da contagem
    return -> sem retorno
    contador - conta começando em i até f com passo p
    """
    while i<=f:
        print(i,end=' => ')
        i += p
    print('FIM')

#contador(10,100,8)
#help(contador)

#Parâmetros opcionais
def soma(a=0,b=0,c=0): #valores usados caso o programa não os informe
    s = a + b +c
    print(f'A soma vale {s}')
    return s
res = soma()
print(res)
#Escopo Local e Global

def teste():
    global b #usado váriavel dentro da função mas como global
    b = 4
    x = 5
    print(f'Na funcão X vale {x}')
    print(f'Na função A vale {a}')

a = 3
b = 2
print(f'No programa principal A vale {a}')
print(f'No programa B vale {b} - A.F.')
teste()
print(f'No programa principal A vale {a}')
print(f'No programa principal b vale {b} - D.F')
#print(f'No programa X vale {x}') X é local e não pode ser usado fora da função

