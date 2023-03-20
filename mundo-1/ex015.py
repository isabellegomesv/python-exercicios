''' Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a 
quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro
custa R$60 por dia e R$0,15 por Km rodado. '''

print('*-' * 15)
print('    ALUGUEL DE CARROS LTDA')
print('*-' * 15)

dias = int(input('Dias alugados: '))
km = float(input('Quantidade de Km percorridos: '))
preco = (dias * 60) + (km * 0.15)
print(f'Você alugou um carro por {dias} dias e percorreu {km}Km e ' 
    f'terá que pagar o total de R${preco:.2f}')
