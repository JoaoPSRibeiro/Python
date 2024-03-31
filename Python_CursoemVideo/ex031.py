"""
Desenvolva um programa que pergunte a distância de uma viagem em KM. Calcule o preço da passagem cobrando R$ 0,50 por KM até 200 KM
e R$ 0.45 por Km acima de 200 km
"""
distancia = float(input('Digite a distancia em KM: '))
menor = distancia * 0.50
maior = distancia * 0.45

if distancia <= 200:
    print('O Valor da passagem será R$ {:.2f}.'.format(menor))
else:
    print('O valor da passagem será R$ {:.2f}.'.format(maior))