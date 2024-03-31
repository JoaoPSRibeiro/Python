"""
Escreva um programa que leia uma frase do teclado e mostre:
1 - Quantas vezes aparece a letra A
2 - Em que posição ela aparece a primeira vez
3 - Em que posição ela aparece a última vez
"""

nome = str(input('Digite a frase que quer analisar: \n'))

print('A letra A aparece {} vezes.\n'.format(nome.upper().count('A')))
print('A letra A aparece pela primeira vez na prosicão {}.\n'.format(nome.upper().find('A')+1)) #soma 1 na exibição da posição da letra A
print('A letra A aparece pela última vez na posição {}.\n'.format(nome.upper().rfind('A')))  #soma 1 na exibição da posição da letra A

# Somar mais um facilitará aou usuário LER o número onde está a letra pesquisada. Sem essa soma, a psição será sempre -1