''' Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.'''

preco = float(input('Digite o preço do produto: R$'))
desconto = preco - (preco * 5 / 100)
print(f'Parabéns!! Você ganhou um desconto de 5% o valor do produto passou de '
    f'R${preco:.2f} para R${desconto:.2f}.')
