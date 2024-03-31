"""
Crie um programa que mostre na tela todos os números pares que estão no intervalo entre 1 e 50
"""

for n in range(1,51):
    if n%2 == 0:
        print(n, end=' ')
print('\nFim\n')

print('Outra forma de fazer o mesmo programa: \n')

for n in range(2, 51, 2):
    print(n, end=' ')
print('\nFIM')