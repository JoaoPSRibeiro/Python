""" 
Calculando comissão usando if, elif e else
"""
vendas = float(input('Digite o valor total das vendas: R$ '))
com_total = vendas * 15 / 100
com_min = vendas * 7.5 / 100

if vendas >= 2000:
    print('Sua comissão será R$ {:.2f} por ter vendido R$ {:.2f} este mês. Parabéns.'.format(com_total, vendas))
elif vendas >= 1500:
    print('Quase conseguiu heim. Suas vendas foram de R$ {:.2f} e sua comissão será de R$ {:.2f}.'.format(vendas, com_min))
else:
    print('Este mês você não alcançou o mínimo, se esforce mais!')
