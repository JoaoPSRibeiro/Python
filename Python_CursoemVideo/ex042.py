"""
Refaça o desafio 35 acrescentando o recurso de mostraro tipo de triangulo que será formado:
- Equilátero == todos os lados iguais
- Isósceles == dois lados iguais
- Escaleno == todos os lados diferentes
"""
r1 = float(input('Digite o tamanho do 1º segmento: '))
r2 = float(input('Digite o tamanho do 2º segmento: '))
r3 = float(input('Digite o tamanho do 3º segmento: ')) 

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos acima podem formar um triângulo', end=' ')          
    if r1 == r2 == r3:
        print('e ele é Equilátero.')
    elif r1 != r2 != r3 != r1:
        print('e ele é Escaleno.') 
    else:
        print('e ele é Isósceles.')
else:
    print('Os Segmentos não formam um triângulo!')