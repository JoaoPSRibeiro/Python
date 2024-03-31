'''
Crie um programa que vaie ler v ários números e colocar em uma lista, Depois disso mostre:
a - Quantos números foram digitados
b - A lista de valres ordenada de forma decrescente
c - Se o valor 5 foi digitado e está ou não na lista
'''
valores = []
while True:
    valores.append(int(input('Digite um valor: ')))
    resp = str(input('Deseja Continuar? [S/N]'))
    if resp in 'Nn':
        break
print(f'Você digitou {len(valores)} elementos.')
valores.sort(reverse=True)
print(f'A lista de valores em ordem decrescente é {valores}')
if 5 in valores:
    print('O número 5 foi digitado e está ns lista.')
else:
    print('O Número 5 não foi digitado e não está na lista.')