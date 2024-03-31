"""
Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do 
jogador e quantas partidas ele jogou. Depois irá ler quantos gols fez por partida. No final, tudo isso 
será adicionado em um dicionário, incluindo o total de gols feitos no campeonato
"""
def linhas():
    print('-=' * 30)
    print('--' * 30)
    print()

jogador = dict()
partidas = list()
jogador['nome'] = str(input('Digite o nome do Jogador: '))
tot = int(input(f'Quantas partidas {jogador["nome"]} participou? '))
for c in range (0,tot):
    partidas.append(int(input(f"    Quantos gols na partida {c+1}: ")))
jogador['gols'] = partidas[:] # copiando partidas dentro de gols
jogador['total'] = sum(partidas) # Soma nº de gols armazenados
linhas()
print(jogador)
linhas()
for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}.')
linhas()
print(f'O Jogador {jogador["nome"]} jogou {len(jogador["gols"])} partidas.')
linhas()
for i,v in enumerate(jogador['gols']):
    print(f'Na partida {i+1} ele fez {v} gols.')
linhas()
print(f'Foi um total de {jogador["total"]} gols.')