""""
A confederação nacional de nataçãoprecisa de um programa que leia o ano de nascimento de um atleta e mostre a sua categoria
de acordo com a sua idade.
 - até 9 anos == mirim ok

 - até 14 anos == infantil ok 

 - até 19 anos == junior ok

 - até 25 anos == senior  ok
 - mais de 25 anos == master
"""
""" 
Outra maneira é importar o datetime e year, criar uma variável 'pegando o ano atual' e outra com o ano de nascimento para assim gerar 
a idade da pessoa.
"""

idade = float(input('Digite a sua idade: '))
if idade <= 9:
    print('Sua Categoria é Mirim!\n')
elif idade >9 and idade < 14 :
    print('A Categoria é Infantil!\n')
elif idade > 14 and idade <= 19:
    print('A Categoria é Junior!\n')
elif idade > 19 and idade <= 25:
    print('A Categoria é Senior!\n')
elif idade > 25:
    print('A Categoria é Master!\n')
else:
    print('O Valor inserido é inválido!')