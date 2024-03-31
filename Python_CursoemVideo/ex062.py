"""
Melhore o desafio 61 perguntando ao usuário se ele quer mostrar mais alguns termos.
O programa encerra quando o usuário digitar que que mais 0 termos
"""

print('GERADOR DE PA')
print('-=' * 20 )
primeiro = int(input('Digite o primeiro termos: '))
razao = int(input('Digite a Razão da PA: '))
termo = primeiro
cont = 1 #contador começa em 1 por que já temos o primeiro termo
total = 0 # somará o total de termos solicitados
mais = 10 # inicia em 10 por que queremos saber os 10 primeiros
while mais != 0:
    total += mais
    while cont  <= total:
        print ('{} → '.format(termo), end='')
        termo += razao
        cont += 1
    print('Pausa')
    mais = int(input('Quantos termos quer mostrar a mais? '))
print('Progressão finalizada com {} termos mostrados.'.format(total))
