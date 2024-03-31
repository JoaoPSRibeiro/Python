"""
Desenvolva um programa que leio o nome, a idade e o sexo de quatro pessoas e no final, 
o programa deve mostrar:
--> a Média de Idade do grupo
--> qual o nome do homem mais velho
--> quantas mulheres têm menos que 20 anos
"""
somaidade = 0
mediaidade = 0
maioridadehomem = 0 
nomevelho = ''
totmulher20 = 0 

for pessoa in range (1 , 5):
    print ('---------- {}º Pessoa ----------'.format(pessoa))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M / F]: ')).strip()
    somaidade += idade
    if pessoa == 1 and sexo in 'Mn':
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maioridadehomem:
        maioridadehomem= idade
        nomevelho = nome
    if sexo in'Ff' and idade < 20:
        totmulher20 +=1
   
mediaidade = somaidade / 4

print(somaidade)
print('A média de idade do grupo é de {} anos.'.format(mediaidade))
print('O homem mais velho tem {} e seu nome é {}.'.format(maioridadehomem, nomevelho))
if totmulher20 >=2 :
    print('No grupo, existem {} mulheres abaixo dos 20 anos.'.format(totmulher20))
elif totmulher20 == 1:
    print('No grupo, existe {} mulher abaixo dos 20 anos.'.format(totmulher20))
else:
    print('Não existe nenhuma mulher menor de 20 anos no grupo!!!')