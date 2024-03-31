"""
Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária 
para pintá-la. Cada 1 litro de tinta pinta 2 metros quadrados
"""
alt = float(input('Digite a altura da Parede: '))
lar = float(input('Digite a largura da Parede: '))
area = alt * lar
tinta = area / 2

print('Sua parede tem {}m de altura e {}m de largura e uma área de {}m quadrados.'.format(alt, lar, area))
print('A parede com {}m de altura e {}m de largura, precisará de {:.2f} litros de tinta para ser pintada.'.format(alt, lar, tinta))