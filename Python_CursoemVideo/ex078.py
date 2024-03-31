'''
Faça um program que leia 5 valores numéricos e guarde-os em uma lista.\
No final, mostre qual foi o maior e o menor valor digitado e suas respectivas posições na lista
'''

listanum = []
mai = men = 0
for c in range (0,5):
    listanum.append(int(input(f'Digite um valor para a posição {c}: ')))
    if c == 0:
        mai = men = (listanum[c])
    else:
        if listanum[c] > mai:
            mai = listanum[c]
        if listanum[c] < men:
            men = listanum[c]
print('=-' * 30 )
print(f'Você digitou os valores {listanum}')
print(f'O maior valor digitado foi {mai} nas posições ', end='')
for i, v in enumerate(listanum):
    if v == mai:                    # busca o maior valor, atribui a var i e verifica a posição
        print(f'{i}... ', end='')
print() #é uma quebra de linha, uma forma de pular uma linha no programa
print(f'O menor número digitado foi {men} nas posições ', end='')
for i, v in enumerate(listanum):
    if v == men:                     # busca o menor valor, atribui a var i e verifica a posição
        print(f'{i}... ', end='')
print()
