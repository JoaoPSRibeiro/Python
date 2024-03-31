"""
Aprimore o desafio anterior, mostrando no fimal:
A --> A soma de todos os valores pares digitados
B --> A soma dos valores da terceira coluna
C --> O maior número da segunda linhda
"""
matriz = [[0,0,0] , [0,0,0] , [0,0,0]]
spar = mai = scol = 0
# spar == soma dos pares
# mai == maior valor 
# scol == soma dos valores da terceira coluna
# Este primeiro FOR está solicitando ao usuário que informe os valores da matriz
for l in range(0,3): # para linha no range de 0 a 3
    for c in range (0,3): # para coluna no range 0 a 3
        matriz[l][c] = int(input(f'Digite um valor para [{l} , {c}]: '))
print('-=' * 30)
# Este segundo for está percorrendo a matriz para montá-la e exibi-la na tela
for l in range(0,3):
    for c in range(0,3):
        print(f'[{matriz[l][c]:^5}]', end="") # O termo :^5 indica que cada célula da matriz ocupa 5 caracteres
        if matriz[l][c] % 2 == 0:
            spar += matriz[l][c]
    print() # este print faz a quebra da linha, fazendo com que a a matriz fique organizada por linha e colunas
print('-=' * 30)
print(f'A soma dos valores pares é {spar}.')
for l in range (0,3): 
    scol += matriz[l][2] #Aqui definimos que queremos os valores da coluna de índice 
print(f'A soma dos valores da terceira coluna é {scol}')    
for c in range(0,3):
    if matriz[1][c] > mai:
        mai = matriz[1][c] # Aqui definimos que queremos o valor da linha
print(f'O maior número da segunda linha é {mai}')