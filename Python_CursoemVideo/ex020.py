""" 
O mesmo professor quer sortear a ordem de apresentação dos trabalhos. Faça um programa que leia os nomes e mostre na tela a ordem sortead
"""
import random
n1 = str(input('Digite o primeiro nome: '))
n2 = str(input('Digite o segundo nome: '))
n3 = str(input('Digite o terceiro nome: '))
n4 = str(input('Digite o quarto nome: '))

lista = [n1, n2, n3, n4]

ordem = random.shuffle(lista) #o Shuffle faz uma reordenação dos ítens, mudando a ordem inicial

print('\nA ordem de apresentação será: ')
print(lista)