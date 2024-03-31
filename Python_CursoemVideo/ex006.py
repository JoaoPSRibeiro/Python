"""
Crie um algoritmo que leia um número e mostre seu dobre, triplo e rais quadrada
"""

num = int(input('Insira um número: '))
dob = num * 2
tri = num * 3
raiz = num ** (1/2)

print('O dobro de {} é {:.2f} !'.format(num, dob))
print('O triplo de {} é {:.2f} !'.format(num, tri))
print('A Raiz Quadrada de {} é {:.2f} !\n'.format(num, raiz)) #coloquei o \n antes do último format para ficar mais legível no terminal