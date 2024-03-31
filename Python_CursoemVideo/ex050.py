"""
Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares,
se o valor digitado for ímpar, desconsidere-o
"""

cont = 0
soma = 0

for c in range(1 , 7):
    num = int(input('Digite o {}º valor: '.format(c)))
    if num % 2 == 0:
        soma += num
        cont += 1

print('Você informou {} pares e a Soma entre eles foi {}.'.format(cont, soma))