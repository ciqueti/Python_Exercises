lad = float(input('Digite a medida do lado da parede: '))
alt = float(input('Digite a medida da altura da parede: '))
area = lad*alt
print('Sua parede tem {}m de largura e {}m de altura. \nTotalizando uma área de {}m2 vocë precisará de {:.2f} litros de tinta'.format(lad,alt,area,area/2))