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
    print(f'Quem nasceu em {nascimento} tem {idade} anos em {atual}.')

    if idade == 18:
        print('Você tem que se alistar imediatamente!')
    elif idade < 18:
        saldo = 18 - idade
        print(f'Ainda faltam {saldo} anos para o alistamento')
        ano = atual + saldo
        print('Seu alistamento será em {}'.format(ano))
    else:
        saldo = idade - 18
        print(f'Você já deveria ter se alistado há {saldo} anos.')
        ano = atual - saldo
        print(f'Seu alistamento foi em {ano}.')
