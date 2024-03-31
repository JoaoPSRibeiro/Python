"""
Crie um programa que mostre na tela a contagem regressiva para o estou de fogos de artificio indo de 10 a 0, com uma pauda
de 10 segundos entre eles
"""
from time import sleep

for count in range(10, -1, -1):
    print (count)
    sleep(1)
print ('Boom, Bo0m, Boom')