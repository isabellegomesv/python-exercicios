''' Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre 
quantos dólares ela pode comprar. '''

real = float(input('Quantos reais você tem na carteira? R$'))

# Dolar hoje 5.29
dolar = real / 5.29
print(f'Com R${real:.2f} você pode compra US${dolar:.2f}')
