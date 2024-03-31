#import math
from math import hypot

co = float(input('Digite o valor do Cateto Oposto: '))
ca = float(input('Digite o valor do Cateto Adjacente: '))
hi = hypot(co , ca)

print('O valor da Hipotenusa é {:.2f} !'.format(hi))