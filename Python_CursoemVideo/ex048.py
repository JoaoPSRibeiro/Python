"""
Faça um programa que calcule a soma entre todos os números ímpares que 
são múltiplos de 3 e que se encontram no intervalos entre 1 e 500
"""
cont = 0 
soma = 0

for c in range(1, 501, 2):
    if c % 3 == 0:
        cont = cont + 1 # cont += 1
        soma = soma + c # soma += c

print('A Soma dos {} valores solicitados é {}.'.format(cont, soma))