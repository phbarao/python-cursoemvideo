from datetime import date

atual = date.today().year
nasimento = int(input('Ano de Nascimento: '))
idade = atual - nasimento

print('O atleta tem {} anos.'.format(idade))

if idade <= 9:
    print('Classificação: MIRIM')
if idade <= 14:
    print('Classificação: INFANTIL')
if idade <= 19:
    print('Classificação: JUNIOR')
if idade <= 25:
    print('Classificação: SÊNIOR')
else:
    print('Classificação: MASTER')
