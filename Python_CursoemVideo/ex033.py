from time import sleep
"""
Faça um programa que leia 3 números e mostre o Menor e o Maior
"""
a = int(input('Insira o Primeiro valor: '))
b = int(input('Insira o Segundo Valor: '))
c = int(input('Insira o Terceiro valor: '))

print('Estamos analisando as possibilidades...')
sleep(3)
print('Analisado!!!\n')

menor = a #aqui definimos que o A é o menor número
if b < a and b < c:
    menor = b # como b é menor que  a e c, a variável agora é B
if c < a and c < b:
    menor = c # como C é menor que os outros, a variável tem este valor agora
maior = a  # aqui, definimos que o maior é o A
if b > a and b > c:
    maior = b 
if c > a and c > b:         #aqui é o mesmo processo que em cima, só que invertido !!!
    maior = c

print('O Menor número é o {}'.format(menor))
print('O Maior número é o {}'.format(maior))