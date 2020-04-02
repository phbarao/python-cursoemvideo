# outra maneira seria criar variaveis para dobro, triplo e raiz.

n = int(input('Digite um número: '))

print('O dobro de {} é {}.'.format(n, n * 2), end=' ')
print('O triplo de {} é {} e'.format(n, n * 3), end=' ')
print('a raíz quadrada é {:.2f}.'.format(n ** (1/2)))
