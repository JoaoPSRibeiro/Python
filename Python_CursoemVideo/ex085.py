"""
Crie um programa onde o usuário possa digitar sete valores
numéricos e cadastre-os em uma lista única que mantenha separado os valores pares e 
ímpares. no final, mostres os valores parese ímpares em forma crescente
"""
valor = 0
todos = [[],[]] #Aqui definimos 2 grupos dentro da lista
for c in range(1, 8):
    valor = int(input(f"Digite o {c}º valor: "))
    if valor % 2 == 0:
        todos[0].append(valor) # Aqui, adicinamos o valor ao item 0 da lista todos
    else:
        todos[1].append(valor) # Aqui ao item 1 da lista
print('-=' * 30)
print(f'A lista completa de valores é: {todos}')
# todos[0].sort()       # esta forma funciona também para ordenar, mas usei direto no print!!!
# todos[1].sort()
print(f'Os valores pares foram {sorted(todos[0])}.')
print(f'Os valores impares fora {sorted(todos[1])}')