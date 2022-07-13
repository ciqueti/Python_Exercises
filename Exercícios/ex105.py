#Exercício Python 105: Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e vai retornar um dicionário com as seguintes informações:
#Quantidade de notas
# A maior nota
# A menor nota
# A média da turma
# A situação (opcional)


def notas(*n,sit=False):
    """
    Função notas - retorna dicionário com maior, menor, média de notas, e opcionalmente a sitação do aluno
    *n - lista com notas
    sit - Parâmetro opcional 
    """
    media = 0
    l = {}
    l['maior_nota'] = max(n)
    l['menor_nota'] = min(n)
    for i in n:
        media += i/len(n)
    l['media'] = media
    if media < 6:
        sit1 = 'Reprovado'
    elif media < 8:
        sit1 = 'Aprovado'
    elif media <= 10:
        si1 = 'Aprovado com excelência'
    if sit == True:
        l['sit'] = sit1
    return l


a = notas(1,5,3,4,sit=True)
print(a)