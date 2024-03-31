""" 
Escreva um programa que pergunte o salárioi  de um funcioinário  e calcule o valor do seu aumento.
Para salários superiores a R$ 1250,00, calcule aumento de 10%
Para salários inferiores a R$ 1250,00 calcule aumento de 15%
"""

salario = float(input('Insira o valor do seu salário Atual: R$ '))

if salario <= 1250 :
    novo = (salario * 15 /100) + salario
else:
    novo = (salario * 10 / 100) + salario

print("Seu novo Salário é R$ {:.2f} !!!".format(novo))


#elif salario > 1250 :
 #   novo = (salario * 10 / 100) + salario
  #  print('Seu novo Salário será R$ {:.2f} !!!'.format(novo))