salario = float(input('Qual é o salário do funcionário? R$ '))
reajuste = 15

novo_salario = salario + (salario * reajuste / 100)

print(f'Um funcionário que ganhava R$ {salario:.2f}, com {reajuste}% de aumento passa a receber R${novo_salario:.2f}')
