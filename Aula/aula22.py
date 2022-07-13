#Usando módulos importados
import moduls

num = int(input('Digite um número: '))
s1 = moduls.fatorial(num)
s2 = moduls.dobra(num)
s3 = moduls.quadruplica(num)

print(f'O fatorial de {num} é {s1} \nO dobro de {num} é {s2} \nO quadruplo de {num} é {s3} ')
