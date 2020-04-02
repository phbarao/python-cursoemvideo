largura = float(input('Largura da parede: '))
altura = float(input('Altura da parede: '))

area = altura * largura
rendimento = area / 2

print('Sua parede tem a dimensão de {}m x {}m e sua área é de {:.2f}m².'.format(largura, altura, area))
print('Para pintar esta parede, você precisará de {:.2f}l de tinta.'.format(rendimento))
