print('Gerador de PA')
print('-=' * 20)

termo = int(input('Primeiro termo: '))
razao = int(input('Razão da PA: '))
cont = 1
total = 0
mais = 10

while mais != 0:
    total += mais
    while cont <= total:
        print('{} -> '.format(termo), end='')
        termo += razao
        cont += 1
    print('PAUSA')
    mais = int(input('Quantos termos você quer mostrar a mais? '))

print('Progressão finalizada com {} ternos mostrados.'.format(total))
