'''
Crie um programa que leia vários números pelo teclado. O programa vai parar quando o usuário digitar 999, que é a condição de parada.
No final, mostre quantos números foram digitados e a soma entre ele, desconsiderando o 999
'''
num = soma = cont = 0 
while True:
    num = int ( input ('Digite um número -> [Digite 999 para Parar]:  '))
    if num == 999:
        break
    cont += 1
    soma += num
print(f'\nForam digitados {cont} números e a Soma entre eles é {soma}.')