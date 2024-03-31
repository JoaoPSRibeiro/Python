""" 
Escreva um programa que leia o cateto oposto e o cateto adjacente de um triangulo retangulo, calcule e mostre o comprimento da 
hipotenusa

O quadrado da hipitenusa é igual a sma dos quadrados dos catetos
"""
co = float(input('Valor do Cateto Oposto: '))
ca = float(input('Valor do Cateto Adjacente: '))
hi = (co**2 + ca ** 2) ** (1/2) #co ao quadrado + ca ao quadrado elevado ao quadrado
print('A hipotenusa é {:.2f}.'.format(hi))

