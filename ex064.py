cont = soma = 0
num = int(input('Digite um número inteiro (999 para parar): '))

while num != 999:
    soma += num
    cont += 1
    num = int(input('Digite um número inteiro (999 para parar): '))

print('Você digitou {} números e a soma deles é igual a {}.'.format(cont, soma))
