casa = float(input('Valor da casa: R$ '))
salário = float(input('Salário do comprador: R$ '))
anos = int(input('Quantos anos de financiamento? '))
prestação = casa / (anos * 12)
mínimo = salário * 30 / 100

print(f'Para pagar uma casa de R${casa:.2f} em {anos} anos,', end='')
print(f' a prestação será de R${prestação:.2f}')

if prestação <= mínimo:
    print('Empréstimo APROVADO!')
else:
    print('Empréstimo NEGADO!')
