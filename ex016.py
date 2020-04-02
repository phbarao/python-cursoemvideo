#Uma opcao simplificada para resolver esse exercicio seria através do int(num) ao inves do trunc(num)

from math import trunc

num = float(input('Digite um valor: '))

print('O valor digitado foi {} e a sua porção inteira é {}'.format(num, trunc(num)))
