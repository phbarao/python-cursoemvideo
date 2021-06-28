num = int(input('Digite um número: '))
total = 0

for c in range(1, num + 1):
    if num % c == 0:
        print('\033[34m', end='')
        total += 1
    else:
        print('\033[31m', end='')
    print(f'{c} ', end='')

print(f'\n\033[mO número {num} foi divisível {total} vezes ', end='')

if total == 2:
    print('e por isso ele É PRIMO!')
else:
    print('e por isso ele NÃO É PRIMO!')
