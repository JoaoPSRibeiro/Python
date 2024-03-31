"""
Faça um algoritmo que leia o salário do funcionário e mostre o seu novo salário com 15% de aumento
"""
sal = float(input('Insira o valor do salário atual: R$ '))
novo_sal = sal * 15 / 100 + sal

print('O funcionário que recebe R${:.2f} passará a receber R$ {:.2f} como o aumento de 15%.'.format(sal, novo_sal))