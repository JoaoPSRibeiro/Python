'''
Crie um programa que teha uma tupla com várias palavras (Não utilizar acento).
depois disso, você deve mostrar, para cada palavra, quais são suas vogais
'''

palavras = ('Aprender', 'Programar', 'Linguagem','Python', 'Curso',
            'Gratis', 'Estudar', 'Praticar', 'Trabalhar', 'Mercado', 
            'Programador', 'Futuro', 'Itanhaem')

for p in palavras: # este laço irá imprimir cada palavra em uma linha separada
    print(f'\nNa palavra {p.upper()} temos: ', end='')
    for letra in p: # este laço busca letras nas palavras
        if letra.lower() in 'aeiou': # Este IF "pega" somenrte as vogais que são a condição neste caso e abaixo impirime essas vogais
            print(letra.lower(), end=' ')