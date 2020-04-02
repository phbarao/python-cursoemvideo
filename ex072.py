cont = ('zero', 'um', 'dois', 'três', 'quatro',
        'cinco','seis', 'sete', 'oito', 'nove', 'dez')

while True:
    num = ' '
    while num not in range (0,11):
        num = int(input('Digite um número inteiro entre 0 e 10: '))
    else:
        print(f'Você digitou o número {cont[num]}')
        resp = ' '
        while resp not in 'SN':
            resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
        if resp == 'N':
            break

print('PROGRAMA FINALIZADO')
