"""
Escreva um programa que leia o nome completo de uma pessoa e diga se tem "Silva" no nome.
"""
nome = str(input('Escreva seu nome completo: '))
print('Seu nome possui Silva?\n')

print(nome.upper().find('SILVA')) # Resulta a posição inicial do Silva, caso não tenha, resulta -1

print('\nSILVA' in nome.upper()) # Resulta True ou False