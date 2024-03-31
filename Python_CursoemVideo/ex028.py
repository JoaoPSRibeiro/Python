""""
Escreva um progra que faça o computador "pensar" em um número de 0 a 5 e peça para o usuário descobrir qual foi o número escolhido.
O programa deve escrever na tela se o usuário venceu ou não 
"""

from time import sleep #fará o computador "dormir", dando a sensação de que está pensando
from random import randint #para randomizar número inteiro

computador = randint(0 , 5)
print('\033[33m-=-\033[m' * 20)
print('\033[31mVou pensar em um número de 0 a 5. Tente adivinhar!!!\033[m')
print('\033[33m-=-\033[m' * 20)

jogador = int(input('\nEm que número eu pensei ?  '))
print('Processando...')
sleep(3)
if computador == jogador:
    print('Uau, que demais. Você adivinhou e me venceu!!')
else:
    print('Ahá, não conseguiu e eu ganhei!!!\nEu pensei no número {} e não no {}.\n'.format(computador, jogador))
