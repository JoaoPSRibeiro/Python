"""
Escreva um programa que leia 2 múmeros inteiros e compare-os mostrando na tela uma mensagem:
- O Primeiro valor é maior
- O Segundo valor é maior
- Nao existe maior, eles são iguais
"""
n1 = float(input('Digite o primeiro valor: '))
n2 = float(input('Digite o segundo valor: '))

if n1 > n2:
    print('O PRIMEIRO valor é maior!!!')
elif n2 > n1:
    print('O SEGUNDO valor é maior!!!')
else:
    print('Não existe maior, eles são IGUAIS!!!')