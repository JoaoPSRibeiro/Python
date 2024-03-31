"""
calculando comissão usando case
"""
vendas = float(input('Insira o valor das vendas: R$ '))

min = vendas * 5 /100
med = vendas * 7.5 / 100
alt = vendas * 10 / 100
pro = vendas * 15 / 100

if vendas >= 1000:
   print(min)
elif vendas >= 1300:
    print(med)
elif vendas >= 1500:
    print(alt)
elif vendas >= 2000:
    print(pro)
else:
    print('Tente outra vez!!!')

"""match vendas:
    case 1000:
        print ('Comissão {}'.format(min))
    case 1300:
        print('Comissão {}'.format(med))
    case 1500:
        print('Comissão {}'.format(alt))
    case 2000:
        print('Comissão {}'.format(pro))
    case _:
        print ("Que pena. Se esforce mais")
"""

#Existe alguma forma de usar o case  em  intervalos como este ???