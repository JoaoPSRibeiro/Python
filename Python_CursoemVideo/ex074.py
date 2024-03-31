'''
Crie um programa que vai gerar 5 números aleatórios. Depois disso, mostre a listagem de números gerador, o maior e o menor.
'''

from random import randint

num = ((randint(1,10)), randint(1,10), randint(1,10), 
       randint(1,10), randint(1,10))

print (f'A lista de números que foi gerada é {num}. ', end='')
print(f'Tendo como menor {min(num)} e maior {max(num)}.')