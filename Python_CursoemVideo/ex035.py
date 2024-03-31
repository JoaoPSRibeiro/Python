"""
Escreva um programa que leia o comprimento de 3 retas e diga ao usuário se elas podem ou nào formar um triângulo
"""
# Cada segmento de um triangulo é menor que a soma do0s outros dois

print('==*==' * 20)
print('Analisador de Triângulos')
print('==*==' * 20)

r1 = float(input('\nPrimeiro Segmento: '))
r2 = float(input('Segundo Segmento: '))
r3 = float(input('Terceiro Segmento: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos acima podem formar um Triângulo!!!\n')
else:
    print('Os segmentos acima não formam um triângulo\n')


# Lembrando 
# AND só é True se tudo for TRUE
# OR é TRUE se um deles for TRUE