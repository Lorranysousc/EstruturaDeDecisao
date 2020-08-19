print('8. Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, sabendo que a decisão é sempre pelo mais barato.\n')

produto1 = float(input('1º Produto \nValor R$'))
produto2 = float(input('2º Produto \nValor R$'))
produto3 = float(input('3º Produto \nValor R$'))
#Testando possibilidades
if produto2 > produto1 < produto3:
    produto_mais_barato = '1º Produto'
    valor = produto1
elif produto1 > produto2 < produto3:
    produto_mais_barato = '2º Produto'
    valor = produto2
else:
    produto_mais_barato = '3º Produto'
    valor = produto3
print(f'\nVocê deverá comprar o {produto_mais_barato} por R${valor:.2f}.')
