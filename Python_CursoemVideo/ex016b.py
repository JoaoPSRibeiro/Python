"""
Crie um programa que leia um número real(float) qualquer e mostre na tela sua parte inteira
"""
from math import trunc
num = float(input('Digite um valor parasaber sua parte inteira: '))
print ('O valor diditado foi {} e sua parte inteira é {} !'.format(num, trunc(num)))
print ('O valor digitado foi {} e sua parte inteira é {:.0f} !'.format(num, num)) #Aqui não usei o trunc, nem criei uma nova variáriel, só eliminei as casas decimais
