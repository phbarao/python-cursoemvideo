salario = float(input('Qual é o salário do funcionário? R$ '))
reajuste = 15

novo_salario = salario + (salario * reajuste / 100)

print('Um funcionário que ganhava R${:.2f}, com {}% de aumento passa a receber R${:.2f}'.format(salario, reajuste, novo_salario))
