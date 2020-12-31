# Script que pergunta o nome da pessoa e diz "muito prazer" com esquema de cores

nome = input('Digite seu nome: ')

cores = {
    'azul': '\033[1;34m',
    'limpa': '\033[m'
}

print('É um prazer te conhecer, {}{}{}!'.format(
    cores['azul'], nome, cores['limpa']))
