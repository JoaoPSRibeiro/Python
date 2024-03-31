"""
Faça um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar
"""
reais = float(input('Quanto dinheiro você tem? R$ '))
dolares = reais / 3.27

print('Com R$ {} você pode comprar US$ {:.2f}.'.format(reais, dolares)) # com definição de casas decimais 
print('Com R$ {} você pode comprar US$ {}.'.format(reais, dolares)) # sem sefinicão de casas decimais
# colocar :.2f faze com que hajam apenas 2 casas decimais em float