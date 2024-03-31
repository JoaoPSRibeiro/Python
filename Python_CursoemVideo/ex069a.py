tot18 = toth = totm20 = 0
while True:
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo: [M/F] ')).strip().upper()[0] #tira os espaços antes e depois, coloca tudo em maísculo e pega só o primeiro caracter
    if idade >= 18:
        tot18 += 1
    if sexo == 'M':
        toth += 1
    if sexo == 'F' and idade <20:
        totm20 += 1
    resp = ' '    
    while resp not in 'SN':
        resp = str(input('Deseja Continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
print(f'O total de pessoas com  mais de 18 anos foi: {tot18}')
print(f'O Total de homens cadastrados foi: {toth}')
print(f'O Total de mulheres com menos de 20 anos foi: {totm20}')