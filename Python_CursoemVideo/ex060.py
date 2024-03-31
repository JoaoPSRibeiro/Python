"""
Faça um programa que leia um número qualquer e mostre seu fatorial
ex: 5! = 5 x 4 x 3 x 2 x 1 = 120
"""

fato = int(input('Digite um nº '))
resultado = 1
count = 1
while count <= fato:
    resultado *= count
    count += 1
print('O Fatorial de {} é {}.'.format(fato, resultado))