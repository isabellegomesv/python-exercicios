''' Elabore um programa que calcule o valor a ser pago por um produto,
considerando o seu preço normal e condição de pagamento:

-  à vista dinheiro/cheque: 10% de desconto
-  à vista no cartão: 5% de desconto
-  em até 2x no cartão: preço normal 
-  3x ou mais no cartão: 20% de juros '''

print('==' * 15)
print(f'{"PYTHON ATACADÃO":^30}')
print('==' * 15)

preco = float(input('Valor da compra: R$'))
pagamento = int(input('''Formas de pagamento:
[ 1 ] À vista dinheito/cheque
[ 2 ] À vista no cartão
[ 3 ] Em até 2x no cartão
[ 4 ] 3x ou mais no cartão
Qual opção desejada? '''))

if pagamento == 1:
    desconto = preco - (preco * 10 / 100)
    print(f'Você recebeu 10% de desconto! Suas compras sairam por R${desconto:.2f}')
elif pagamento == 2:
    desconto = preco - (preco * 5 / 100)
    print(f'Você recebeu 5% de desconto! Suas compras sairam por R${desconto:.2f}')
elif pagamento == 3:
    print(f'Suas compras sairam por R${preco / 2:.2f} cada parcela SEM JUROS.')
elif pagamento == 4:
    total = preco + (preco * 20 / 100)
    parcelas = int(input('Quantas parcelas? '))
    print(f'Você parcelou suas compra em {parcelas} vezes de R${total / parcelas} COM JUROS '
    f'resultando em um total de R${total}')
else:
    print('[ERRO] Opção invalida! Tente novamente.')
