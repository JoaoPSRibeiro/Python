"""
Crie um programa que leia uma frase qualquer e diga se ela é um palíndrono, desconsiderando os espaços
PALÍNDRONO == frase ou palavra que oode ser lida da esquerda para a direita e também o contrário
AnA, Osso, RadaR...
Apos a sopA, A sacasa da casA, A torre da derrota, O lobo ama bolO
"""
frase = str(input('Digite uma frase ou palavra: ')).strip().upper()
#Frase não não tem mais espaços denreo de dela e também, está toda em maiúscula
palavras = frase.split()
#criamos uma lista com as palavras da frase
junto = ''.join(palavras)
#juntamos todas as palavras em uma nova 'frase' sem espaços entre elas
inverso = ''
for letra in range (len(junto)-1, -1, -1):
    #para letra no intervalos de junto - 1, indo até 0 sempre tirando 1
    inverso += junto[letra]

if inverso == junto:
    print('Temos um Palíndrono')
else:
    print('A frase digitada não forma um Palíndrono.')
print('O inverso de {} é {}!'.format(junto, inverso))