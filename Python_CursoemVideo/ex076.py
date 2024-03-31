'''
Crie um programa que tenha uma tupla única com uma listagem de produtos e seus respsctivos preços na sequência.
no final, mostre uma listagem dos preços, organizados de forma tabular.
'''
listagem = ('Lápis', 1.75,
            'Borracha', 2,
            'Caderno', 15.90,
            'Estojo', 25,
            'Transferidor', 4.20,
            'Compasso', 9.99,
            'Mochila', 120.32,
            'Canetas', 22.30,
            'Livro', 34.90,)
print('-' * 40)
print(f'{"LISTAGEM DE PREÇOS":^40}') # Esta frase estará centralizada dentro de um espaço de 40 caracteres
print('-' * 40)

for pos in range (0,  len(listagem)):
    if pos % 2 == 0:
        print(f'{listagem[pos]:.<30}', end='')
        # Se a posição (dentro do index) for PAR imprima do lado esquerdo e complete 30 caracteres usando o . como espaçador
    else:
        print(f'R$ {listagem[pos]:>7.2f}')
        # Se a posição for IMPAR, imprima usando 7 caracteres alinhados a direita com 2 pontos flutuantes