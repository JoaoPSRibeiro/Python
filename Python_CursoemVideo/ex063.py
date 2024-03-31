""""
Escreva um programa que leia um número n inteiro qualquer e mostre na tela os n primeiros números de uma sequência Fibonacci
ex: 0 -> 1 -> 1 -> 2 -> 3 -> 5 -> 8 (leia  0+ 1 = 1, 1 + 1 = 2, 1 + 2 = 3, 2 + 3 = 5, 3 + 5 = 8 etc )

A Sequencia Fibonacci é uma sequência numéria em que p 1 termo é o resiultado da soma ds 2 anteriores
"""

print('-' * 40)
print('{: ^40}'.format('Sequência Fibonacci'))
print('-' * 40)
n = int(input('Digite quantos termos você quer mostrar: '))
t1 = 0
t2 = 1
print('~' * 40)
print('{} -> {}'.format(t1, t2), end='')
cont = 3
while cont < n:
    t3 = t1 + t2
    print(' -> {}'.format(t3), end='')
    t1 = t2
    t2 = t3
    cont += 1
print(' -> FIM')
print('~' * 40)