print('-=' * 20)
print('Analisador de Triângulos'.upper())
print('-=' * 20)

s1 = float(input('Primeiro segmento: '))
s2 = float(input('Segundo segmento: '))
s3 = float(input('Terceiro segmento: '))

print('-=' * 20)

if s1 < s2 + s3 and s2 < s1 + s3 and s3 < s1 + s2:
    print('Os segmentos acima PODEM formar triângulo!')
else:
    print('Os segmentos acima NÃO PODEM formar triângulo!')
