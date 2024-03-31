'''
Crie um programa onde o usuário irá digitar 5 valores numéricos e cadastre-os em uma lista já na posição correta
sem o uso do sort()
No final mostre q lista ordenada na tela
'''

lista = []
for c in range(0 , 5):
    n = int(input('Digite um valor: '))
    if c == 0 or n > lista [-1]: #se o contador for igual a zero ou o n for maior que o tamanho total da lista, faça
        lista.append(n)
        print('Adicionado ao fim da lista')
    else:
        pos = 0
        while pos < len(lista): #Enquanto POS for menor que o tamanho da lista
            if n <= lista[pos]:
                lista.insert(pos, n) # Se o valor de n for menor que o valor que esta em pos, coloque N em pos
                print(f'Adicionado à posição {pos} da lista')
                break
            pos += 1
print('=-' * 30)
print(f'Os valores digitados em ordem foram {lista}')