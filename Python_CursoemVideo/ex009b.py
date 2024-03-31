"""Escreva um programa que leia um número qualquer e mostre na tela a sua tabuada """
num = int(input('Insira um valor: '))
aux = 0
print('_' * 15)
print('A Tabuada do número {} é:'.format(num))
print('_'* 15)

while (aux <= 10):
    print('{} x {} = {}'.format(num, aux, num * aux))
    aux = aux + 1