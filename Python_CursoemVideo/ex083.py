'''
Crie um programa onde um usuário digite uma expressão qualquer que use parenteses.
Seu aplicativo deverá analisar se a expressão passada está om os parenteses abertos e fechados na ordem correta.
'''
expressao = str(input('Digite a expressão matemática: '))
pilha = []
for simb in expressao:
    if simb == '(':
        pilha.append('(')
    elif simb == ')':
        if len(pilha) > 0:
            pilha.pop() #tira o último ítem da lista PILHA
        else:
            pilha.append(')')

if len(pilha) == 0: # Aqui o código identifica que para cada parentes que abriu, houve um fechando
    print('Sua expressão é válida!')
else:
    print('Sua expressão está incorreta e é inválida.') # Aqui não, aqui mostra que há parentese sobrando, o que é errado!!!