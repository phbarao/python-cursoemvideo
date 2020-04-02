from math import hypot

catOposto = float(input('Comprimento do cateto oposto: '))
catAdjacente = float(input('Comprimento do cateto adjacente: '))
hip = hypot(catOposto, catAdjacente)

print('A hipotenusa vai medir {:.2f}'.format(hip))
