"""
Crie um programa que leia vários números inteiros pelo teclado, o programasó vai parar quando o usuário digitar 999.
No final mostre quantos números foram digitados e qual foi a soma entre eles, descontando a flag
"""
print('-' * 30)
num = cont = soma = 0
while True:
    num = int (input ('Digite um número: '))
    if num == 999:
        break
    cont += 1
    soma += num
print(f'A Soma dos valores digitados foi {soma}')
print(f'Fora digitados {cont} números')