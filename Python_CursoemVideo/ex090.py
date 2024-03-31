"""
Faça um programa que leia nome e média de um aluno, guardando também a situação do aluno
em um dicionário. NO final mostre o conteúdo da estrutura na tela.
"""

aluno = dict() # pode ser aluno = {}
aluno['nome'] = str(input('Nome: ')) # Criada a chave nome e pedindo valor
aluno['media'] = float(input(f'Média de {aluno["nome"]}: ')) # Criada a chave média e pedindo valor
if aluno['media'] > 7:
    aluno['situacao'] = 'Aprovado' # Criamos a chave Situação a atribuimos o valor Aprovado
elif 5 <= aluno['media'] < 7:
    aluno['situacao'] = 'Recuperação' # Criamos a chave situação e atribuimos o valor Recuperação
else:
    aluno['situacao'] = 'Reprovado' # Aqui, a chave situação receberá o valor reprovado
print ('-=' * 30)

for k, v in aluno.items():
    print(f'{k}:  {v}')

print ('-=' * 30)
