#lanche = () - tupla [] - lista {} - dicionário
lanche = ('Hamburger', 'Suco', 'Doce-de-Leite', 'Canastra')
print(lanche[2])
print(lanche[-1])
print(lanche[1:3])
print(lanche[-3:])
#Tuplas são imutáveis
#lanche[1] = 'Salada'
print(lanche[1])
for i in (lanche):
    print(f'Eu comerei {i} esta manhã')
print(len(lanche))
for cont in range (1, len(lanche)):
    print(cont)
for i in range (0,len(lanche)):
    print(f'Nesta tupla temos - posição {i} comida {lanche[i]}')
for pos,comida in enumerate(lanche): #dado + posição
    print(f'Eu vou comer {comida} que está na posição {pos} ')
print((sorted(lanche)))
print(lanche)

a = (2,1,8,6,7)
b = (1, 2, 3)
c = a + b
print(c)
print(c.count(2))
#c = sorted(a+b)
print(c)
print(c.index(8))
cao = ('Albert', 33, 88.2, 'M') #
print(type(cao[0]))
print(type(cao[1]))
print(type(cao[2]))
del(cao) #Deletar Tupla