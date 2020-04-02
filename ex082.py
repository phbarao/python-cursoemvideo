lista = []
pares = []
ímpares = []

while True:
    n = int(input('Digite um número: '))
    lista.append(n)
    if n % 2 ==0:
        pares.append(n)
    else:
        ímpares.append(n)
    resp = str(input('Quer continuar? [S/N]'))
    if resp in 'Nn':
        break

print('=-' * 30)
print(f'A lista completa é {lista}')
print(f'A lista de pares é {pares}')
print(f'A lista de ímpares é {ímpares}')
