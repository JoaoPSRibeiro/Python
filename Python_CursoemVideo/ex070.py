'''
Crie um programa que leia o nome e o preço de vários produtos.
O programa deverá perguntar se o usuário deseja continuar e no final mostrar:
a - qual o total gasto na compra
b - quantos produtos custam mais que R$ 1000,00
c - qual o nome do produto mais barato
'''
total = totmil = menor = cont = 0 # todas as variáveis iniciam com o mesmo valor, por isso são declaradas dessa forma
barato = ' ' # esta é a variável do produto mais barato e é uma String Vazia

while True:
    produto = str(input('Digite o nome do produto: '))
    valor = int(input('Digite o valor do produto: R$ '))
    cont +=1
    total += valor
    if valor > menor:
        menor = valor
    if valor > 1000:
        totmil += 1
    if cont == 1 or valor < menor:
        menor = valor
        barato = produto
    continuar = str(input('Deseja Cadastrar mais produtos? [S/N]')).upper().strip()[0]
    print('--' * 20 )
    if continuar == 'N':
        break

print(f'O Valor total gasto na compra foi R$ {total}')
print(f'O produto mais barato é {barato}')
print(f'Temos {totmil} produtos custando mais de R$ 1000,00')