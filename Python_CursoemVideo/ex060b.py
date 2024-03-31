"""Faça um programa que leia um número qualquer e mostre seu fatorial
ex: 5! = 5 x 4 x 3 x 2 x 1 = 120
"""
from math import factorial
n = int(input('Digite o número que deseja saber o fatorial: '))
f = factorial(n)
print ('O Fatorial de {} é {}.'.format(n , f))
print (f'O Fatorial de {n} é {f}. FORMATADO COM FSTRING')