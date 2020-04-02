from random import randint

print('=-' * 15)
print('VAMOS JOGAR PAR OU ÍMPAR?')
print('=-' * 15)

vitorias = 0

while True:
    pc = randint(0,10)
    jogador = int(input('Digite um valor: '))
    total = jogador + pc
    tipo = ' '
    while tipo not in 'PI':
        tipo = input('Par ou Ímpar? [P/I] ').strip().upper()[0]
    print(f'Você jogou {jogador} e o computadpr {pc}. Total de {total}. ', end='')
    print('DEU PAR' if total % 2 == 0 else 'DEU ÍMPAR')
    if tipo == 'P':
        if total % 2 == 0:
            print('Você VENCEU!')
            vitorias += 1
        else:
            print('Você PERDEU!')
            break
    elif tipo == 'I':
        if total % 2 != 0:
            print('Você VENCEU!')
            vitorias += 1
        else:
            print('Você PERDEU!')
            break
    print('Vamos jogar novamente...')

print(f'GAME OVER! Você venceu {vitorias} vezes.')
