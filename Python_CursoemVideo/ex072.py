'''
Crie um programa que tenha uma tupla totalmente preenchida por uma contagem de zero a vinte popr extenso.
O Programa deverá leer um númeto no teclado, de zero a vinte, e mostrar o correnpondente, por extenso na tela
'''

cont = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis',
        'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 
        'catorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito',
        'dezenove', 'vinte')
while True:
    num = int(input('Digite um número entre 0 e 20: '))
    if 0 <= num <=20:
        break
    print('Tente Novamente: ')
print(f'Você digitou o número {(cont[num]).upper()}') # Aqui ele associa as duas informações, procurando com CONT, o valor relacionado ao índice NUM