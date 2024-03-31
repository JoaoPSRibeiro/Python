"""
Crie um programa que leia o nome completo de uma pessoa e mostre:
    O nome com todas as letras Maiúsculas e Minúsculas.
    Quantas letras tem ao todo.
    Quanitas Letras tem o primeiro nome.
"""
nome = str(input('Digite seu nome completo: '))
print ('Olá {}, vamos analisar seu nome ?'.format(nome))
print('\nSeu nome escrito em letras Maiúsculas é {}'.format(nome.upper()))
print('\nSeu nome escrito com letras minúsculas é {}'.format(nome.lower()))
print('\nSeu nome tem {} letras sem contar os espaços!!'.format(len(nome)-nome.count(' ')))
print('\nSeu primeiro nome tem {} letras.'.format(nome.find(' ')))

separa = nome.split()
print('\nSeu primeiro nome é {} e ele tem {} letras!!!\n'.format(separa[0], len(separa[0])))