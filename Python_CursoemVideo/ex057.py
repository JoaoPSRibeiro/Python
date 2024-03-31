"""
Faça um programa que leia o sexo de uma pessoa, mas só aceite valores 'M' ou 'F'.
Caso entre com valor diferente, peça para digitar novamente até ter um valor correto
"""
"""m = ''
f = ''

sexo = ''
while sexo != m != f:
    sexo = str(input('Digite o sexo [M / F]: ')).lower()
    if sexo == m:
        m = sexo
    elif sexo == f:
        f = sexo
    else:
        print('Valor inválido, tente novamente')

print('Feito!!!')"""

sexo = str(input('Informe seu sexo: [M/F] ')).strip().upper()[0]
while sexo not in 'MmFf':
    sexo = str(input('Dados inválidos. Por favor, informe seu sexo: ')).strip().upper()[0]

print('O sexo {} foi registrado com sucesso.'.format(sexo))