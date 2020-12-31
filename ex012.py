preço = float(input('Qual é o preço do produto? R$ '))

desconto = 5
preço_final = preço - ((preço * desconto) / 100)

print(f'O produto que custava R${preço:.2f}, na promoção com desconto de {desconto}% vai custar R${preço_final:.2f}.')
