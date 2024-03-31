"""
Crie um programa que faça o computador jogar JOKENPO com você!
"""
from random import randint
from time import sleep

itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0,2) #randomiza do ítem 0 ao 2

print ("""Escolha uma opção:
[0] Pedra
[1] Papel
[2] Tesoura
""")
jogador = int(input('Digite a opção escolhida: '))

print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO')

print('-=' * 11)
print('-=' * 11)
print('Computador escolheu {}.'.format(itens[computador]))
print('Jogador escolheu {}.\n'.format(itens[jogador]))

if computador == 0: #Computador escolheu Pedra
    if jogador == 0:
        print('Os dois escolheram pedra!!! Empate')
    elif jogador == 1:
        print('Jogador escolheu Papel e Ganhou!!!')
    elif jogador == 2:
        print('Computador Ganhou!!!')
    else:
        print('Opção Inválida')
elif computador == 1: #Computador jogou Papel
    if jogador == 0:
        print('Computador venceu')
    elif jogador == 1:
        print('Os dois escolheram papel!! Empate!')
    elif jogador == 2:
        print('Jogador venceu!!!')
    else:
        print('Opção Inválida')
elif computador == 2:
    if jogador == 0:
        print('Jogador venceu')
    elif jogador == 1:
        print('Computador venceu!')
    elif jogador == 2:
        print('Empate!')
    else:
        print('Opção Inválida!')
