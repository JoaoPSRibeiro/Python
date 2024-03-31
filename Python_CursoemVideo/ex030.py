"""
Crie um programa que diga se um número é par ou ímpar
"""
num = int(input('Digite um número para saber se ele é par ou ímpar: '))
result = num % 2

if result == 0:
    print('O Número digitado foi \033[31m{}\033[m e ele é \033[1;32mPAR\033[m.\n'.format(num)) #inserindo cor no terminal
else:
    print('O número digitado foi {} e ele é Ímpar!\n'.format(num))