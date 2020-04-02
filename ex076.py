produtos = ('Lápis', 1.75,
            'Borracha', 2,
            'Caderno', 15.90,
            'Estojo', 25,
            'Mochila', 120.32,
            'Livro', 34.90,
            'Canetinhas', 22.30)

print('-' * 40)
print(f'{"LISTAGEM DE PRODUTOS":^40}')
print('-' * 40)

for position in range(0, len(produtos)):
    if position % 2 == 0:
        print(f'{produtos[position]:.<30}', end='')
    else:
        print(f'R${produtos[position]:>6.2f}')

print('-' * 40)
