while True:
    num = int(input('Digite um número para ver sua taboada: '))
    if num < 0:
        break
    print('-' * 50)
    for c in range(1,11):
        print(f'{num} x {c} = {num * c}')
    print('-' * 50)

print('-' * 50)
print('Acabou!')
