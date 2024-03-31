"""
Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, mostre uma menagem dizendo que ele foi
multado.
A multa vai custar R$ 7,00 por Km/h acima do limite
"""

carro = float(input('Qual a velocidade? '))
limite = 80
multa = (carro - limite) * 7 

if carro > 80:
    print('Sua velocidade medida foi de \033[31m{} Km/h\033[m e a multa a ser paga é de R$ {:.2f}.\n'.format(carro, multa))
else:
    print('A velocidade medida foi {} km/h.\n'.format(carro))
print('Dirija com responsabilidade!!!\n')