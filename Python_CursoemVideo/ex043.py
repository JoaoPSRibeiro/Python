"""
Dezenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule o imc e mostre seu status de acordo com  a tabela abaixo:
- abaixo de 18,5 -> abaixo do peso
- entre 18,5 e 25 -> peso ideal
- de 25 a 30 -> sobre peso
- de 30 a 40 -> obesidade
- acima de 40 -> obesidade mórbida
"""
peso = float(input('Digite seu peso em Quilos: '))
altura = float(input('Digite sua altura em Metros: '))
imc = peso / (altura ** 2)

if imc < 18.5:
    print ('Seu IMC é de {:.2f} e você está MUITO abaixo do peso.'.format(imc))
elif 18.5 <= imc <25:
    print ('Seu IMC é de {:.2f} e você está em seu peso Ideal !!!'.format(imc))
elif 25 <= imc < 30:
    print ('Seu IMC é de {:.2f} e você está um pouco acima do peso, se cuide!!!'.format(imc))
elif 30 <= imc < 40:
    print ('Seu IMC é de {:.2f} e você está acima do peso. Procure um médico ou faça uma dieta!'.format(imc))
elif imc >= 40:
    print ('Seu IMC é de {:.2f} e você está excessivamente acima do peso. Procure um médico URGENTE.'.format(imc))