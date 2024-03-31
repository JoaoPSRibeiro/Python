"""
Um professor que sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome deles e
escrevendo o oscolhido tela.
"""

import random
n1 = str(input('Digite o primeiro nome: '))
n2 = str(input('Digite o segundo nome: '))
n3 = str(input('Digite o terceiro nome: '))
n4 = str(input('Digite o quarto nome: '))

lista = [n1, n2, n3, n4]

sorteado = random.choice(lista) #Chama o Random e usa O CHOICE para fazer o sorteio

print('\nO Aluno escolhido para apaga a lousa foi: {} !!!'.format(sorteado))
