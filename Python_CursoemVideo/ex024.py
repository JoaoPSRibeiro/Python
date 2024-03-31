"""
Faça um programa que leia o nome de  uma cidade e diga se ela começa ou não com "Santo"
"""
print('Sua cidade começa com Santo??? \n')
nome = str(input("Digite o nome da sua cidade: \n")).strip()

print(nome[:5].upper() == 'SANTO')


"""
# acrescentando algo além da aula em si
cidade = nome[:5].upper() == 'SANTO'
if cidade == True:
    print("Sim começa com Santo\n")
else:
    print('Sinto muito, não começa com "Santo"!!\n')
"""