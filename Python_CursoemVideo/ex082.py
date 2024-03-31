'''
Crie um programa que vai ler vário números e colocar em uma lista.
Depois disso, crie duas listas extras que vão conter apenas os números pares e os números impares.
ao final, mostre os valores das três listas geradas
'''
num = list()
pares = list()
impares = list()

while True:
    num.append(int(input('Digite um valor: ')))
    resp = str(input('Deseja continuar? [S/N]'))
    if resp in 'Nn':
        break
for i,v in enumerate(num):
    if v % 2 == 0:
        pares.append(v)     #aqui verificamos numero por numero e o colocamos na variável correta, par o impar
    elif v % 2 == 1:
        impares.append(v)
print('=-' * 30)
print(f'A lista completa de valores digitados é {num}.')
print(f'A lista de valores PARES digitados é {pares}.')
print(f'A lista de valores ÍMPARES digitados é {impares}.')
      