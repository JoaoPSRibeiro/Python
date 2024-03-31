"""
Desenvolva um programa que leia duas notas de um aluno e mostre a média desses valores:
"""

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
media = (n1 + n2) / 2

print('A média das notas {} e {} foi: {} !\n'.format(n1, n2, media))

""" 
Incrementando a aula
"""

if media >= 6:
    print('E você foi aprovado! Parabéns!!!\n')
else:
    print('Reprovado. Tente novamente!!!\n')