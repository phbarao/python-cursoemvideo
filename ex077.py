#CONTADOR DE VOGAIS

palavras = ('aprender', 'programar', 'python', 'curso', 'gratis', 'estudar', 'praticar', 'trabalhar')

for p in palavras:
    print(f'\nNa palavra {p.upper()} temos ', end='|')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra, end='|')
