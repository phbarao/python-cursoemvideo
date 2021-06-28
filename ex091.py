from random import randint
from time import sleep
from operator import itemgetter

ranking = ()

jogo = {'Jogador1': randint(1,6),
        'Jogador2': randint(1,6),
        'Jogador3': randint(1,6),
        'Jogador4': randint(1,6)}


print('Valores sorteados: ')
for jogador, numeroSorteado in jogo.items():
    print(f'{jogador} tirou {numeroSorteado} no dado.')
    sleep(0.8)

ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)

print('-=' * 30)
print(' == RANKING DOS JOGADORES ==')

for counter, numeroSorteado in enumerate(ranking):
    print(f'    {counter + 1}º lugar: {numeroSorteado[0]} com {numeroSorteado[1]}.')
    sleep(0.8)
