"""
Faça um programa que leia o peso de 5 pessoas. no final mostre qual foi o maior e qual foi o menor
"""
menor = 0
maior = 0

for pessoa in range (1,6):
    peso = float(input('Digite o peso da {}º pessoa: '.format(pessoa)))
    if pessoa == 1:
        menor += peso
        maior += peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('O maior peso foi {} Kg e o menor foi {} Kg.'.format(maior, menor))