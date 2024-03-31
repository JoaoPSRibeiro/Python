'''
Crie um programa que simule o funcionamento de um caixa eletrônico.
No início, pergunte ao usuário qual o valor a ser sacado e o programa irá informar quantas cédulas de cada valor serão entregues
Obs.: Considere apenas cédulas de 50.00, 20.00, 10.00, 1.00
'''
print('-' * 30)
print('{:^30}'.format('Banco  CEV')) # A String, banco cev, irá ocupar 30 espaços e estará centralizado nesses 30 caracteres
print('-' * 30)

valor = int(input('Que valor desejas sacar? R$ '))
total = valor
ced =  50 #Cédula inicia em 50
totalced = 0 # programa inicia com nenhuma cédula

while True:
    if total >= ced:
        total -= ced #se o total for maior que a cédula, subtrair do total o valor da cédula e em totalced adiciona 1
        totalced += 1
    else:
        if totalced > 0:
            print(f'\nO total de {totalced} cédulas de R$ {ced:>6.2f}')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10: # neste bloco iniciado no  else, vamos atribuindo novos valores à cédula até zerar o valor sacado
            ced = 1
        totalced = 0 
        if total == 0:
            break
print ('-' * 30)
print('Volte sempre ao Banco CV\n')