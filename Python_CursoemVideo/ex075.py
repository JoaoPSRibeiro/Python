'''
Crie um programa que leia 4 númenros pelo teclado e os guarde em uma tupla. nom final mostre
a -> quantas vezes aparece o número 9 - ok
b -> em que posição foi digitado o primeiro valor 3 -- ok 
c -> quais foram os números pares
'''
num = (int(input('Digite um número: ')), int(input('Digite outr número: ')),
        int(input('Digite mais número: ')),  int(input('Digite o último número: ')))
print(f'Você digitou os números {num}.')

# Aqui verifico quantas vezes o nove aparece, guardando na variável cont. 
# sPodemos fazer direto o print, mais assim, trato a possibilidade não não haver o número 9 na tupla
cont = num.count(9)
if cont > 0:
    print(f'O número 9 apareceu {cont} vezes. \n')
else:
    print('O número 9 não foi digitado nehuma vez')

# Abaixo vamos verificar se o número 3 aparece e qual foi a primeira posição "Humana" dele
if 3 in num:
    print(f'O número aparece primeiro na posição {num.index(3) + 1}.')
else:
    print('O número 3 não foi digitado.')

# vamos analisar se tem número par abaixo

print('Os valores pares digitados foram: ', end='')
for n in num:
    if n % 2 == 0:
        print(n, end=', ')