'''
from math import factorial

n = int(input('Digite um número inteiro: '))

f = factorial(n)
print('O fatorial de {} é {}'.format(n, f))

'''

n = int(input('Digite um número inteiro: '))
c = n
f = 1

print(f'Calculando {n}! = ', end='')

while c > 0:
    print(f'{c}', end='')
    print(' x ' if c > 1 else ' = ', end='')
    f *= c
    c -= 1

print(f'{f}')
