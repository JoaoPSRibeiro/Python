""" 
Faça um programa que leia um Ângulo qualquer e mostre na tela o valor do Seno, Cosseno e a Tangenre desse Ângulo
Seno = Eixo vertical
Cosseno = Eixo Horizontal
Tangente = linha entre os dois
"""

#import math
from math import radians, sin, cos, tan
an = float(input('Digite o Ângulo: '))

seno = sin(radians(an)) # transforma o valor digitado em radianos para podermos calcular 
print('\nO ângulo de {:.2f}° tem o SENO de {:.2f} !'.format(an, seno))

cosseno = cos(radians(an))
print ('O ângulo de {:.2f}° tem o COSSENO de {:.2f} !'.format(an, cosseno))

tangente = tan(radians(an))
print('O ângulo de {:.2f}° tem a TANGENTE de {:.2f} !'.format(an, tangente))