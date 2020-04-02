preço = float(input('Qual é o preço do produto? R$ '))

desconto = 5
preço_final = preço - ((preço * desconto) / 100)

print('O produto que custava R${:.2f}, na promoção com desconto de {}% vai custar R${:.2f}.'.format(preço, desconto, preço_final))
