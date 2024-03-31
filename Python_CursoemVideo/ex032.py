"""
Faça um programa que leia um ano qualquer e diga se ele é bissexto
"""

from datetime import date # importa a biblioteca Date, que é o dia atual

ano = int(input('Digite o ano que quer saber se é Bissexto ou digite 0 para o ano atual: \n'))
if ano == 0:
    ano = date.today().year #esta função "Pega" o ano atual da máquina e atribui à variável ANO

if ano % 4 == 0 and ano % 100 != 0 and ano % 400 == 0: #Esta é a regra matemárica para saber se um ano é bissexto
    print('O Ano {} é BISSEXTO.\n'.format(ano))
else:
    print('O Ano {} não é BISSEXTO.\n'.format(ano))

    """
    ano / 4 == 0 e
    ano / 100 != 0 e            SE ATENDER AOS 3 REQUISITOS, O ANO É BISSEXTO 
    ano / 400 = 0
    """