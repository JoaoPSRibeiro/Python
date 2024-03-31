"""
crie um programe que leia dois valores e exiba o menu
[1] Somar
[2] Multiplicar
[3] Maior número
[4] Começar denovo
[5] Sair do programa
"""
from time import sleep
n1 = int(input('Insira o Primeiro Valor: '))
n2 = int(input('Insira o Segundo Valor: '))
opcao = 0

while opcao != 5:
    print('''Selecione a opção desejada:
      [1] Somar
      [2] Multiplicar
      [3] Maior Número
      [4] Começar denovo
      [5] Sair do Programa
''')
    opcao = int(input('Qual a opção desejada? '))
    if opcao == 1:
        soma = n1 + n2
        print('A soma entre {} e {} é {}.\n'.format(n1,n2,soma))
    elif opcao == 2:
        produto = n1 * n2
        print('A Multiplicação de {} e {} resulta em {}.\n'.format(n1, n2, produto))
    elif opcao == 3:
        if n1 > n2:
            print('O maior número é {}.\n'.format(n1))
        elif n1 < n2:
            print('O maior número é {}.\n'.format(n2))
        else:
            print('Não há menor ou maior, eles são iguais!!!')
    elif opcao == 4:
        print('Escolha novos números: ')
        n1 = int(input('Insira o primeiro Valor: '))
        n2 = int(input('Insira o segundo valor: '))
    elif opcao == 5:
        print('Finalizando')
        sleep (2)
    else:
        print('Opção inválida, tente novamente.\n')
print('=-=' * 10)
print('Fim do Programa, volte sempre.\n')