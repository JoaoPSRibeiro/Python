"""
Refaça  desafio 9, mostrando a tabuada do número informado pelo usuário, só que agpra usando o laço FOR
"""

num = int(input('Digite o valor que quer saber a tabuada: '))

for c in range (1, 11):
    print('{} x {} = {:2}'.format(num, c, num * c))

print('Obrigado e Bons estudos!!!')