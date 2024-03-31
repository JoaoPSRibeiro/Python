"""
Faça um programa que leia o ano de nascimebt de um jovem e informe,  de acordo com a idade, se ele ainda vai se alistar
ao serviço militar, se é a hora de se alistar ou se já passpu o tempo de alistamento. Seu programa deverá mostrar o tempo 
que falta ou que passou.
"""

from datetime import date
atual = date.today().year #"Pega" o ano atual do sistema
nasc = int(input('Digite o ano de seu nascimento: '))
idade = atual - nasc
print('Você nasceu em {} e tem {} anos em {}\n'.format(nasc, idade, atual))

if idade == 18:
    print('Aliste-se imediatamente!!\n')
elif idade < 18:
    saldo = 18 - idade
    print ('Você não tem 18 anos, faltam {} anos para você se alistar.\n'.format(saldo))
elif  idade > 18:
    saldo = idade - 18 
    print('Você tem {} e já se passaram {} anos do seu alistamento.\n'.format(idade, saldo))
