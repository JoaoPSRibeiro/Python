"""
Escreva um programa que converta uma temperatura digita em °C para °F. para fazer o símbolo ° usar ALT + 0176
"""
c = float(input('Digite a Temperatura em °C : '))
f = ((9 * c) / 5) + 32 # 9 vezes a temperatura em celcius dividido por 5 + 32

print('A Temperatura {:.2f}°C corresponde a {:.2f}°F !'.format(c,f))