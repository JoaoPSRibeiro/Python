"""
Desenvolva um programa que leia o primeiro termo e a razão de uma progressão aritmérica.
no final, mostre os 10 primeiros termos dessa prograssão
Razão == 2
Primeiro Termo == 0
PA == 2 , 4, 6 , 8 ...
"""

primeiro = int(input('Digite o Primeiro Termo: '))
razao = int(input('Digite a Razão: '))
decimo = primeiro + (10 - 1) * razao # 10 -1 refere-se ao décimo termo da PA 

for c in range(primeiro, primeiro + razao, razao):
    print('{}'.format(c), end=' -> ')
print('\nACABOU!')