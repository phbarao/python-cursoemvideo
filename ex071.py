print('=' * 30)
print('BANCO CEV')
print('=' * 30)

valor = int(input('Quanto você deseja sacar? R$ '))
print('=' * 30)
total = valor
cédula = 50
totalCédulas = 0

while True:
    if total >= cédula:
        total -= cédula
        totalCédulas += 1
    else:
        if totalCédulas > 0:
            print(f'Total de {totalCédulas} cédulas de R$ {cédula}')
        if cédula == 50:
            cédula = 20
        elif cédula == 20:
            cédula = 10
        elif cédula == 10:
            cédula = 1
        totalCédulas = 0
        if total == 0:
            break

print('=' * 30)
print('Volte sempre ao BANCO CEV! Tenha um bom dia!')
