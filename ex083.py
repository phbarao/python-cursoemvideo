#Crie um programa onde o usuário digite uma expressão qualquer que use parênteses. Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta.

expressão = str(input('Digite a expressão: '))
pilha = []

for símbolo in expressão:
    if símbolo == '(':
        pilha.append('(')
    elif símbolo == ')':
        if len(pilha) > 0:
            pilha.pop() #remover ultimo elemento da lista
        else:
            pilha.append(')')
            break

if len(pilha) == 0:
    print('Expressão válida.')
else:
    print('Expressão inválida.')
