# Programa que pede o valor de 3 variáveis e apresenta sua soma com esquema de cores.

a = int(input('Digite um valor para variável "a": '))
b = int(input('Digite um valor para variável "b": '))
c = int(input('Digite um valor para variável "c": '))

# se remover o tipo primitivo int de antes do input, o programa não irá somar, e sim concatenar os números.

soma = a + b + c

print()
print('\033[1;34;40m A soma dos valores {}, {} e {} é: {}! \033[m'.format(a, b, c, soma))
