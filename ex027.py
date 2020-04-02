nome = str(input('Digite seu nome completo: ')).strip()
separado = nome.split()


print('Muito prazer em te conhecer!')
print('Seu primeiro nome é {}'.format(separado[0].capitalize()))
print('Seu último nome é {}'.format(separado[len(separado)-1].capitalize()))
