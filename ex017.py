from math import hypot

catOposto = float(input('Comprimento do cateto oposto: '))
catAdjacente = float(input('Comprimento do cateto adjacente: '))
hip = hypot(catOposto, catAdjacente)

print(f'A hipotenusa vai medir {hip:.2f}')
