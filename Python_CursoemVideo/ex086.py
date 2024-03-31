"""
crie um programa que crie uma matriz de dimensão 3x3
e preencha com valores lidos pelo teclado
No final, mostre a matriz na tela com  a formatação correta
"""
matriz = [[0,0,0],[0,0,0],[0,0,0]] # Já declaramos a variável matriz com as posições zeradas

for linha in range(0,3):
    for coluna in range(0,3):
        matriz[linha][coluna] = int(input(f'Digite um valor para [{linha}, {coluna}]: '))
         #Na linha acima, solicitamos os números, já pocionando em linha / coluna
print('-=' * 15)
for linha in range(0,3):
    for coluna in range(0,3):
        print(f'[{matriz[linha][coluna]:^5}]', end='')
        # Na linha acima, vamos ordenar nossa matriz, colocando os valores ocupando uma área de 5 dígitos {:^5} centralizados
    print() 