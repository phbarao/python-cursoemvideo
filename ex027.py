nome = str(input('Digite seu nome completo: ')).strip()
separado = nome.split()


print('Muito prazer em te conhecer!')
print(f'Seu primeiro nome é {separado[0].capitalize()}')
print(f'Seu último nome é {separado[len(separado)-1].capitalize()}')
