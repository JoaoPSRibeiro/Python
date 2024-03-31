'''
Faça um program onde o usuário possa digitar vários valores numéricos
e cadastreo-os em uma lista. Caso o número já exista lá dentro, ele não será adicionado.
No final serão exibidos todos os valotres únicos digitados em ordem crescente
'''

numeros = list()
while True:
    n = int(input('Digite um valor: '))
    if n not in numeros:
        numeros.append(n)
        print('Valor adicionado com sucesso!!!')
    else:
        print('Valor duplicado, não vou adicionar este!')
    resp = str(input('Deseja continuar? [S/N]'))
    if resp in 'Nn':
        break
print('=-' * 30)
numeros.sort()  # Ordena os valores em ordem crescente
print(f'Os valores digitados foram {numeros}')