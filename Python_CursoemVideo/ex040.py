"""
Crie um programa que leia duas notas de um aluno e calcule sua média mostrando uma mensagem no final de acordo com a nota obtida:
- Abaixo de 5.0 == Reprovado
- Entre 5.1 e 6.9 == Recuperação
- Acima de 7.0 == Aprovado
"""
print ('--**--' * 10)
print ('SISTEMA DE NOTAS')
print ('--**--' * 10)

nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
media = (nota1 + nota2) / 2

print('Sua Média foi {:.1f} .'.format(media))

if media < 5.0:
    print('E você foi Reprovado. Se esforce mais!')
elif media >= 5.1 and media <= 6.9 :
    print('E Você está de Recuperação. Ainda há uma chance de passar!!!')
elif media >= 7.0:
    print('Você foi Aprovado. Parabéns!!!')
