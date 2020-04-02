from datetime import date

atual = date.today().year
nascimento = int(input('Ano de nascimento:'))
idade = atual - nascimento
sexo = input('''Sexo:
[ M ] Masculino
[ F ] Feminino
''').upper()

if sexo == 'F':
    print('Por ser mulher, o alistamento não é obrigatório')
elif sexo == 'M':
    print('Quem nasceu em {} tem {} anos em {}.'.format(nascimento, idade, atual))

    if idade == 18:
        print('Você tem que se alistar imediatamente!')
    elif idade < 18:
        saldo = 18 - idade
        print('Ainda faltam {} anos para o alistamento'.format(saldo))
        ano = atual + saldo
        print('Seu alistamento será em {}'.format(ano))
    else:
        saldo = idade - 18
        print('Você já deveria ter se alistado há {} anos.'.format(saldo))
        ano = atual - saldo
        print('Seu alistamento foi em {}.'.format(ano))
