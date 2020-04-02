'''

Minha opção:

opcao = 's'

while opcao not in ('Nn'):
    num = str(input('Digite um número: '))
    opcao = str(input('Quer continuar? [S/N]'))

print(opcao)
'''

resposta = 's'
soma = quantidade = media = maior = menor = 0

while resposta in 'Ss':
    num = int(input('Digite um número: '))
    soma += num
    quantidade += 1
    if quantidade == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    resposta = str(input('Quer continuar? [S/N]')).upper().strip()[0]
media = soma / quantidade
print('Você digitou {} números e a média foi {}!'.format(quantidade, media))
print('O maior valor foi {} e o menor valor foi {}'.format(maior, menor))
