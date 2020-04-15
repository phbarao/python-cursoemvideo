def área(largura, comprimento):
    a = largura * comprimento
    print(f'A área de um terreno {largura}x{comprimento} é de {a}m2.')


#Programa Principal
print('Controle de Terrenos')
print('-' * 20)
l = float(input('LARGURA (m): '))
c = float(input('Comprimento (m): '))
área(l, c)
