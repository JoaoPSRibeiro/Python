"""
Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em
uma lisra composta. No fimal mostre um boletim contendo a media de cada um e permita 
que o usuário possa mostrar as notas de cada aluno individualmente
"""
ficha = list()
#Obtendo dados para a lista
while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2) / 2
    ficha.append([nome, [nota1 , nota2], media]) 
    # Acima Estamos inserindo na variável ficha uma lista composta com os dados adquiridos 
    resp = str(input('Quer continuar? [S/N] '))
    if resp in 'Nn':
        break
print('-=' * 30) 
print(f'{"No.":<4}{"NOME":<10}{"MÉDIA":>8}')
# Na linha acima estamos criando um cabeçalho com:
# No. alinhado a esquerda e 4 casas
# NOME alinhado a esquerda, com 10 casas
# MEDIA alinhado a direita com 8 casas e 1 ponto flutuante
print('-' * 26)
for i, a in enumerate(ficha):
    print(f'{i:<4}{a[0]:<10}{a[2]:8.1f}')
    # Nesta linha vamos imprimir os resultado no mesmo padrao do cabeçalho criado
    #pegando o índice[i] da lista, seguido do nome(a[0]) e da media(a[2])
while True:
    print('-' * 35)
    opc = int(input('Mostrar notas de qual aluno (999 para Interromper): '))
    if opc == 999:
        break
    if opc <= len(ficha) -1:
        print(f'Notas de {ficha[opc][0]} são {ficha[opc][1]}')
        # Nesta linha pegamos o nome e as notas para imprimir
print('<<< VOLTE SEMPRE >>>')        