"""
Faça um programa que ajude um jogador da Mega Sena
a criar palpites. O programa vai perguntar queantos jogos serão gerados
e vai sortear 6 números entre 1 e 60 para cada jogo.
cadastrando tudo em uma lista composta
"""
from random import randint
from time import sleep
lista = list() # Lista temporária, onde cada jogo será salvo
jogos = list() # Lista final, onde todos os jogos serão salvos
# as linhas abaixo são enfeite
print('-' * 30)
print('       JOGA NA MEGA SENA     ')
print('-' * 30)
quant = int(input('Quantos jogos você quer que eu sorteie? '))
tot = 1 # número de jogos, será usado no laço, iniciando em 1 para não fazer 1 a mais no final
while tot <= quant:
    cont = 0 #Contador para sortearmos apenas 6 números para cada jogo
    while True:
        num = randint(1, 60)
        if num not in lista: # Aqui garantios que não haverá repetição dos números no jogo
            lista.append(num) #Adicionamos o número à lista
            cont += 1
        if cont >= 6:
            break
    lista.sort() #Ordenando os números sorteados
    jogos.append(lista[:]) # não esquecer de fazer sempre a cópia da lista, ela está sendo apagada na linha de baixo
    lista.clear()
    tot += 1
print(f'Os números sorteados foram: ')
print()
for i, l in enumerate(jogos): #Este laço pega o índice e enumera com a a lista e exibe no print
    print(f'Jogo {i+1}  : {l}')
    sleep(1.2)
print()
print('-=' * 5, '< BOA SORTE >', '-=' * 5)
print()
