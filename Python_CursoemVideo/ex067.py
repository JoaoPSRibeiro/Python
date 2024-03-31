'''
Faça um programa que mostre a tabuada de vários números, 1 de cada vez, para cada valor digitado pelo usuário.O programa será interrompido quando o número digitado for negativo
'''

num = 0
while num >= 0:
    num = int (input('Digite o valor da tabuada: '))
    if num < 0:
            break
    for c in range (1 , 11):
        result = num * c
        print(f'{num} x {c} = {result}')
print('FIM')