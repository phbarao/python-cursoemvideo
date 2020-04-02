primeiro = int(input('Primeiro número: '))
segundo = int(input('Segundo número: '))

if primeiro > segundo:
    print('O maior número é: {}'.format(primeiro))
elif segundo > primeiro:
    print('O maior número é: {}'.format(segundo))
else:
    print('Os números digitados são iguais!')
