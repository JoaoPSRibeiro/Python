"""
melhore o jogo do desafio 28 onde o cpmputador vai 'pensar' em um número entre 0 e 10. Só que agora o jogador vai tentar 
adivinhar até acertar, mostrando no final, quantar temtativas foram necessárias !!!
"""

from random import randint
computador = randint(0,10)
print('Sou seu computador e estou pensando em um número')
print('Você será capaz de avidinhar??')
acertou = False
palpite = 0 

while not acertou:
    jogador = int(input('E qual seu palpite? '))
    palpite += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('\nMais, tente denovo!')
        elif jogador > computador:
                print('\nMenos, tente novamente.')
print('\nUhulll... Você conseguiu e foram necessárias {} tentativas.'.format(palpite))