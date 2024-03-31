"""
Faça um Algoritmo que leia o preço de um produto e mostre o seu novo preço com 5% de desconto
ex: 10 * 5 / 100 = 0.5 ou seja, 5% de 10
ex: 1500 * 10 / 100 = 150 ou seja 10% de 1500
ex: 875 * 15/100 = 131.25 ou seja 15% de 875
"""
preco = float(input('INsira o valor atual do produto: R$ '))
novo_preco = preco - preco * 5 / 100

print('O Produto que vale R$ {} passará a custar R$ {:.2f} com o desconto de 5%.'.format(preco, novo_preco))