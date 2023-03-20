''' Crie um programa que leia o nome e o preço de vários produtos. 
O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:

A) qual é o total gasto na compra.
B) quantos produtos custam mais de R$1000.
C) qual é o nome do produto mais barato. '''

print('==' * 15)
print(f'{"LOJAS PYTHON":^30}')
print('==' * 15)

total = 0
produto_caro = 0
contador = 0
produto_barato_nome = ''
produto_barato_preco = 0

while True:
    nome_produto = input('Digite o nome do produto: ').strip().capitalize()
    preco_produto = float(input('Digite o preço do produto: R$'))
    contador += 1
    print('--' * 15)
    print(f'{"Produto adicionado":^30}')
    print('--' * 15)
    # Total da compra:
    total += preco_produto
    # Produtos acima de R$1000
    if preco_produto >= 1000:
        produto_caro += 1
    # Produto mais barato
    if contador == 1:
        produto_barato_nome = f'{nome_produto}'
        produto_barato_preco = preco_produto
    else:
        if produto_barato_preco > preco_produto:
            produto_barato_nome = f'{nome_produto}'
            produto_barato_preco = preco_produto

    continuar = ' '
    while continuar not in 'SN':
        continuar = input('Você deseja continuar? [S/N] ').upper().strip()
    print('--' * 15)
    if continuar == 'N':
        break

print(f'{"Compra finalizada!":^30}')
print('Obrigada por comprar na Lojas Python!! Aqui está uma análise da sua compra:')
print(f'Total da compra: R${total:.2f}\n'
    f'Produtos acima de R$1000,00: {produto_caro}\n'
    f'Produto mais barato: {produto_barato_nome} por R${produto_barato_preco:.2f}')
