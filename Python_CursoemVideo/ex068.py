'''
Faça um programa que jpgue para ou ímpar com o computador.
O jogo só será interrompido quando o jogador perder, mostrando o tota de vitórias consecutivas que ele conquistou no final do jogo.
'''
from random import randint
v = 0

while True:
    jogador = int(input('Digite um valor: '))
    computador = randint(0,10)
    total = jogador + computador
    tipo = ' '
    
    while tipo not in 'PI':
        tipo = str(input('Par ou Impar ? [P/I]: ')).upper().strip()[0]
    print(f'Você jogou {jogador} e o Computador jogou {computador}. Total de {total}')
    print('DEU PAR' if total % 2 == 0 else 'DEU IMPAR')
    if tipo == 'P':
        if total % 2 == 0 :
            print('Você venceu')
            v += 1
        else:
            print('Você Perdeu!')
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print('Você venceu!')
            v += 1
        else:
            print('Você Perdeu!')
            break
    print('Vamos jogar novamente...')
print(f'Game Over, você teve {v} vitórias')
