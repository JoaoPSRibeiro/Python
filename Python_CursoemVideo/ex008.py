"""Esreva um progtrama que leia um valor em metros e o exiba convertido em centímetros e milímetros """

medida = float(input('Insita um valor em Metros: '))
cm = medida * 100
mm = medida * 1000
dm = medida * 10
dam = medida / 10 
hm = medida / 100
km = medida / 1000
print('A medida {} m corresponde a {} cm e {} mm'.format(medida, cm, mm))
print(dm)
print(dam)
print(hm)
print(km)
#as outras medidas coloquei para mostrar como calcular cada um !!!
""" 
km == Kilometro == 1000 metros
hm == hectometro == 100 metros
dam == Decametro == 10 metros

dm == decimetro ==  1 * 10  metro
cm == centimetro == 1 * 100 metro
mm == milimetro == 1 * 1000 metro
"""