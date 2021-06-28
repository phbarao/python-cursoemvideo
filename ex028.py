from random import randint
from time import sleep

computador = randint(0,5)

print('-=' * 30)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('-=' * 30)

jogador = int(input('Em que número eu pensei? '))

print('\nPROCESSANDO...')
sleep(2)

if jogador == computador:
    print('\nParabéns! Você conseguiu me vencer!')
else:
    print(f'\nGanhei! Eu pensei no número {computador} e não no {jogador}!')
