# Uma opcao simplificada para resolver esse exercicio seria através do int(num) ao inves do trunc(num)

from math import trunc

num = float(input('Digite um valor: '))

print(f'O valor digitado foi {num} e a sua porção inteira é {trunc(num)}')
