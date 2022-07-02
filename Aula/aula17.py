#Listas e Mais
n = [1,7,9,43]
n[2] = 5 #Listas são mutáveis
#n.append(777)
print(n)
#n.sort(reverse=True) #Parämetro para ordenar de forma decrescente
n.pop(2)
n.insert(1,2)
n.insert(4,2)
if 2 in n:
    n.remove(2)
print(n)
print(f'A lista {n} possui {len(n)} elementos!')

valores = []
valores.append(1)
valores.append(-10)
valores.append(7)
for p,v in enumerate(valores):
    print(f'Enontrei o valor {v} na posição {p}')
print('Final da Lista')
valores = list()

#Adicionando valores do usuário em uma Lista
for c in range (1,4):
    valores.append(int(input('Digite um número - ')))
print(valores)

#Ligação e Cópia entre Listas

a = [2,'peixe',-7,9,5]
#b = a #Ligação entre listas
b = a[:] #B recebe os valores de A, temos uma cópia
b[3] = 27 #Teste as duas linhas acima separadamente 
print(f'Lista A - {a}') 
print(f'Lista B - {b}')
