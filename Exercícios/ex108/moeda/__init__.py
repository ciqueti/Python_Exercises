def aumentar(valor,taxa,formatacao = False):
    valor *= 1 + taxa/100
    if formatacao == True:
        return(moeda(valor))
    return(valor)

def diminuir(valor,taxa,formatacao = False):
    valor *= 1 - taxa/100
    if formatacao == True:
        return(moeda(valor))
    return(valor)

def metade(valor,formatacao = False):
    valor *= 1/2
    if formatacao == True:
        return(moeda(valor))
    return(valor)

def dobro(valor, formatacao = False):
    valor*= 2
    if formatacao == True:
        return(moeda(valor))
    return(valor)

def moeda(valor=0,moeda='R$'):
    return f'{moeda}{valor:.2f}'.replace('.',',')

def resumo(valor=0, taxa=0):
    print('='*30)
    print(f'{"RESUMO":^30}')
    print('='*30)
    print(f'Preço Analisado - {moeda(valor)}')
    print(f'Dobro do Preço - {dobro(valor,True)}')
    print(f'Aumento {taxa}% - {aumentar(valor,taxa,True)}')
    print(f'Diminuir {taxa}% - {diminuir(valor,taxa,True)} ')