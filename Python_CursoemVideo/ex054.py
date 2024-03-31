"""
Crie um programa que leia o ano de nascimento de sete pessoas. No final mostre quantas pessoas ainda não atingiram a maioridade (21 anos) 
e quantas já são maiores
"""
from datetime import date
atual = date.today().year

totmaior = 0
totmenor = 0

for pessoa in range (1, 8):
    nasc = int(input('Digite o Ano em que a {}º pessoa nasceu: '.format(pessoa)))
    idadeatual = atual - nasc

    if idadeatual >= 21:
        totmaior += 1
    else:
        totmenor += 1

print("{} pessoas são maiores de idade e {} são menores.".format(totmaior, totmenor))