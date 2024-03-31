"""
Crie um programa qu e leia o nome, ano de nascimento, carteira de trabalho e cadastre-os
(com idade) em um dicionário. Se, por acaso, a CTPS for diferente de zero, o dicionário receberá também o ano de 
contratação e o salário. Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.
"""
from datetime import datetime
dados = dict()
dados['nome'] = str(input('Nome: '))
nasc = int(input('Ano de Nascimento: '))
dados['idade'] = (datetime.now().year - nasc)
print(dados['idade'])
dados['ctps'] = int(input('Número da CTPS (0 para não tem): '))
if dados['ctps'] != 0:
    dados['contratacao'] = int(input('Ano do primeiro contrato: '))
    dados['salario'] = float(input('Salário: '))
    dados['aposentadoria'] = dados['idade']+ ((dados['contratacao'] + 35)-datetime.now().year)
print('-=' * 30)

for k, v in dados.items():
    print(f'{k} tem o valor: {v}')