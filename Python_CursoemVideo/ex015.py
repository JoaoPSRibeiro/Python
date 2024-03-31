"""
Escreva um programa que pergunte a quantidade de Kilometros percorridos por um carro alugado e
a quantidade de dias pelos quais foi alugado. Calcule o preço a pagar, sabendo que o carro custa 
R$ 60,00 por dia e R$ 0.15 porkm rodado.
"""
dias = int(input('Digite o número de dias: '))
km = float(input('Digite a kilometragem percorrida: '))
total = (dias * 60) + (km * 0.15)
print('O valor a ser pago pelo aluguel do carro é {:.2f}!'.format(total))