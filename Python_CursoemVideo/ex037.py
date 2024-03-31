"""
Escreva um programa que leia um númenro inteiro qualquer e peça para o usuário escolher que a base de conversão:
 - 1 para Binário
 - 2 para Octal
 - 3 para Hexadecimal
"""
num = int(input('Digite o número que quer converter: '))
print('''Para qual Base você quer converter?\n
      [ 1 ] para BINÁRIO
      [ 2 ] para OCTAL
      [ 3 ] para HEXADECIMAL\n''')
escolha = int(input('Qual o número escolhido ? '))

if escolha == 1:
    print('O valor {} convertido para BINÁRIO fica {}.'.format(num, bin(num)[2:]))
elif escolha == 2:
    print('O Valor {} convertido para OCTAL fica {}.'.format(num, oct(num)[2:]))
elif escolha == 3:
    print('O Valor {} convertido para HEXADECIMAL fica {}.'.format(num, hex(num)[2:]))
else:
    print('Valor Inválido.\n')
