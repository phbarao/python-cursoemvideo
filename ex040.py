nota1 = float(input('Primeira nota: '))
nota2 = float(input('Segunda nota: '))
media = (nota1 + nota2) / 2

print('Tirando {:.1f} e {:.1f}, a média do aluno é {:.1f}'.format(nota1, nota2, media))

if 7 > media >= 5:
    print('O aluno está em recuperação.')
elif media < 5:
    print('O aluno está reprovado.')
elif media >= 7:
    print('O aluno está aprovado.')
