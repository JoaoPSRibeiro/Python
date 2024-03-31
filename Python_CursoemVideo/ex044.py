"""
Elabore um programa que calcule o valor a ser pago por um produto, considerando seu preço normal e a condição
de pagamento:

à vista -> dinheiro, cheque ou Pix == 10% de desconto
à vista -> cartão de débito ou crédito == 5% de desconto
em até 2x no cartão == preço normal
3x ou mais no cartão == 20% de juros
"""

print('{: ^40}'.format('Lojas JP'))
preco = float(input('Digite o valor total das compras em R$: '))
print("""Selecione a forma de Pagamento:
[1] À Vista (Dinheiro/Cheque/Pix)
[2] À Vista Cartão (Débito ou Crédito)
[3] 2x no Cartão
[4] 3x ou mais no Cartão""")

opcao = int(input('Qual a opção selecionada? '))

if opcao == 1:
    preco = preco - (preco * 10 / 100)
    print('O Valor a ser pago é R${:.2f} à vista, já com 10% de desconto!\n'.format(preco))
elif opcao == 2:
    preco = preco - ( preco * 5 / 100)
    print('O Valor a ser pago é R$ {:.2f} à vista, já com 5% de desconto!\n'.format(preco))
elif opcao == 3:
    parc = preco / 2
    print('Sua compra de R$ {:.2f} será parcelada em 2 vezes de R$ {:.2f} cada parcela.'.format(preco, parc))
elif opcao == 4:
    novopreco = preco + (preco * 20 /100)
    parc = novopreco / 4
    print('Sua compra de R$ {:.2f} será parcelada em 4 vezes de R$ {:.2f} já com acréscimo de 20% no valor total da compra, totalizando o valor de R$ {:.2f}.\n'.format(preco, parc, novopreco))
else:
    print('Opção Inválida\n')