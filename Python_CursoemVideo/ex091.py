""" 
Faça um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. Guarde esses
resultados em um dicionário. No final coloque este dicionário em ordem, sabendo que o vencedor tirou o maior número do dado.
"""
from operator import itemgetter # essa biblioteca será usada para ordenar o dicionário
from random import randint # gerador de números aleatórios
from time import sleep # Para criar a pausa!!

jogo = {
    'jogador1': randint(1,6),
    'jogador2': randint(1,6),
    'jogador3': randint(1,6),
    'jogador4': randint(1,6)}
ranking = list() # esta variável vamos usar para rankear os jogadores
print()
print('Valores Sorteados: ')
for k,v in jogo.items():
    print(f'{k} tirou {v} no dado.')
    sleep(1)

ranking = sorted(jogo.items(), key = itemgetter(1), reverse = True)
# Para ordenar o dicionário precisamos importar o itemgetter. Iremos ordenar pelo valor do dicionário e não pela chave.

print('-=' * 30)
for i, v in enumerate(ranking):
    print(f'{i + 1}º lugar = {v[0]} com {v[1]}. ') # para o indide mais 1, nome do jogador e valor sorteado
    sleep(1)