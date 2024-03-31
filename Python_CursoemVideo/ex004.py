"""Faça um programa que leia algo pelo teclado, mostre na tela seu tipo primitivo e todas as informações sobre ele"""
a = input('Digite algo:')
print('O tipo primitivo desse valor é ', type(a))
print('Só tem espaços? ', a.isspace())
print('É um número? ', a.isnumeric())
print('Tem letras e números? ', a.isalnum())
print('Quantos caracteres possui? ', len(a))
print('Ele está em maiúsculas?', a.isupper())
print('Está em minusculas?', a.islower())
print('Está capitalizado?', a.istitle()) #capitalizado é a forma de começarmos uma frase, ou nome de alguém, algum lugar. Primeira letra maiúscula
