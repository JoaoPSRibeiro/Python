''''
Crie um programa que leia vários números inteiros pelo teclado. No fonal a ewxecução mostre:
- a média entre todos os valores
- qual foi o maior número
- menor número
O programa deve perguhtar se o usuário que continuar ou não
'''
resp = 'S'
soma = quant = media = maior = menor = 0

while resp in 'Ss':
    num = int(input('Digite um valor: '))
    soma += num
    quant += 1
    if quant == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    resp = str(input('Deseja Continuar? [S/N] ')).upper().strip()[0]
    if resp != 'S' and resp != 'N':
        print('Valor Inválido')
        resp = str(input('Deseja Continuar? [S/N] ')).upper().strip()[0]

media = soma / quant
print(f'\nVocê digitou {quant} números e a Média entre eles é {media}.')
print(f'O maior número foi {maior} e o Menor foi {menor}.')