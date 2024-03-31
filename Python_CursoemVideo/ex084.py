""""
Faça um programa que leia o nome e peso de várias pessoas.guardando tudo em uma lista. NO final mostre:
a - quantas pessoas foram cadastradas
b - uma listagem com as pessoas mais pesadas
c - uma listagem com as pessoas mais leves
"""
temp = []
princ = []
maiorP = menorP = 0
while True:
    temp.append(str(input('Nome: ')))
    temp.append(float(input('Peso: '))) 
    #A variável Temp é uma lista, quando damos o append na variável princ, colocamos a lista dentro da lista
    if len(princ) == 0:
        maiorP = menorP = temp[1]
    else:
        if temp[1] > maiorP:
            maiorP = temp[1]
        if temp[1] < menorP:
            menorP = temp[1]
    princ.append(temp[:]) # Aqui fazemos uma cópia do temp para a lista principal
    temp.clear() # Limpamos a variável temp para não copiar a cada volta no laço
    resp = str(input('Desja continuar? [S/N] '))
    if resp in 'Nn':
        break
print('-=' * 30)
print(f'Você cadastrou {len(princ)} pessoas.')
print(f'O Maior peso foi de {maiorP} Kg. Peso de ', end='')
for p in princ:
    if p[1] == maiorP: # Aqui ele verifica se o primeiro item da lista é maior que o MaiorP, se for ele imprime na linha de baixo, se não, ele não faz nada e entra no outro laço abaixo
        print(f'{p[0]} ', end='')
print()
print(f'O Menor peso foi de {menorP} Kg. Peso de ', end='')
for p in princ:
    if p[1] == menorP:
        print(f'{p[0]} ', end='')
print()

