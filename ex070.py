total = mais1000 = menor = cont = 0
barato = ''

print('-' * 20)
print('LOJA SUPER BARATÃO')
print('-' * 20)

while True:
    produto = str(input('Nome do Produto: '))
    preço = float(input('Preço: R$ '))
    cont += 1
    total += preço

    if preço > 1000:
        mais1000 += 1
    if cont == 1 or preço < menor:
        menor = preço
        barato = produto

    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break

print('-' * 20)
print('FIM DO PROGRAMA')
print('-' * 20)
print(f'O total da compra foi R${total:.2f}')
print(f'Temos {mais1000} produtos custando mais de R$ 1.000,00')
print(f'O produto mais barato foi {barato} que custou R${menor:.2f}')
