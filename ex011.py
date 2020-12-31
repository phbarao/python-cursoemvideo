largura = float(input('Largura da parede: '))
altura = float(input('Altura da parede: '))

area = altura * largura
rendimento = area / 2

print(f'Sua parede tem a dimensão de {largura}m x {altura}m e sua área é de {area:.2f}m².')
print(f'Para pintar esta parede, você precisará de {rendimento:.2f}l de tinta.')
