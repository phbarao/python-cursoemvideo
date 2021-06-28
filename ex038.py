primeiro = int(input('Primeiro número: '))
segundo = int(input('Segundo número: '))

if primeiro > segundo:
    print(f'O maior número é: {primeiro}')
elif segundo > primeiro:
    print(f'O maior número é: {segundo}')
else:
    print('Os números digitados são iguais!')
