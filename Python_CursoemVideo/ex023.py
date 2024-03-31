"""
Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos seus digitos separados.
"""
num = int(input("Digite um número entre 0 e 9999: \n"))
uni = num // 1 % 10
dez = num // 10 % 10        
cen = num // 100 % 10
mil = num // 1000 % 10
print('\nO número digitado foi {}.\n'.format(num))
print('A unidade é {}'.format(uni))
print('A dezena é {}'.format(dez))
print('A centena é {}'.format(cen))
print('O milhar é {}\n'.format(mil))