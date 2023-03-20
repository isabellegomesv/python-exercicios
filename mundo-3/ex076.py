''' Crie um programa que tenha uma tupla única com nomes de produtos e 
seus respectivos preços, na sequência. No final, mostre uma listagem de preços, 
organizando os dados em forma tabular. '''

produtos = (
    'Lápis', 1.65, 'Pão', 5.00, 'Salame', 13, 'Caderno', 20, 'Queijo', 9.00,
    'Papel Sulfite', 15, 'Água', 2.50, 'Coca-Cola', 5.50, 'Presunto', 8.00, 'Mortadela', 6.00,
)
print('--' * 17)
print(f'{"Lista de Preços":^32}')
print('--' * 17)
for c, produto in enumerate(produtos):
    if c % 2 != 0:
        print(f'{" R$":.>15}{produto:.2f}')
    else:
        print(f'{produto:.<15}', end='')
print('--' * 17)
    