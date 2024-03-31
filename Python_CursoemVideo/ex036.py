"""
Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. Pergunte o valor da casa, o salário do comprador e em
quantos anos ele irá pagar.
A prestação mensal não pode ultrapassar 30% do salário ou então o empréstimo será negado
"""
casa = float(input('Qual o valor da casa? R$ '))
anos = int(input('Em quantos anos quer pagar? '))
salario = float(input('Qual o salário do comprador? R$ '))
parcelas = casa / (anos * 12)
minimo = salario  * 30 / 100

print('Para pagar uma casa de R$ {:.2f} em {} anos, '.format(casa, anos), end='')
print('a prestação será de R$ {:.2f} !'.format(parcelas))

if parcelas <= minimo: ### O erro e stava aqui
    print('Seu financiamento foi APROVADO')
else:
    print('Seu financiamento foi NEGADO')