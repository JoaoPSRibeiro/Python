'''
Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa adastrada o computador irá perguntar se o usuário quer ou não continuar.
No final mostre:
(a) quantas pessoas tem mais de 18 anos
(b) quantos homens foram cadastrtrados
(c) quantas mulheres tem menos de 20 anos
'''
sexo = ' '
conti = ' '
maiorIdade = totHomens = totMulher20 = 0
while True:
    print('-' * 30)
    print('{: ^30}'.format('CADASTRE UMA PESSOA'))
    print('-' * 30)
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).upper().strip()[0]
    if sexo == 'M':
        totHomens += 1
    if idade >= 18:
        maiorIdade += 1
    elif sexo == 'F' and idade < 20:
        totMulher20 +=1
    conti = str(input('Continuar Gravando dados? [S/N]: ')).upper().strip()[0]
    if conti == 'N':
        break
print(f'Foram cadastrados {totHomens} homens.')
print(f'Existe {totMulher20} mulheres menores de 20 anos.')
print(f'E do total cadastrado, {maiorIdade} tem mais de 18 anos.')