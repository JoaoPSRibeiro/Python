"""
Refaça o desafio  51, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão 
utilizando a estrutura while
"""

print('Gerador de PA')
print('-=' * 10)
primeiro = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))
termo = primeiro 
cont = 1

while cont <= 10:
    print('{} '.format(termo), end=' ')
    termo += razao #soma a razao ao termo, é assim que funciona a PA!!!
    cont += 1
print('FIM')