''' Crie um programa que simule o funcionamento de um caixa eletrônico. 
No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro) 
e o programa vai informar quantas cédulas de cada valor serão entregues. OBS:

considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1. '''

print('==' * 15)
print(f'{"CAIXA ELETRONICO":^30}')
print('==' * 15)

saque = int(input('Digite o valor do saque: R$'))

nota_50 = nota_20 = nota_10 = nota_1 = 0

while saque != 0:
    
    if saque >= 50: # Conferindo notas de 50
        nota_50 += 1
        saque -= 50

    elif saque >= 20: # Conferindo notas de 20
        nota_20 += 1
        saque -= 20
    
    elif saque >= 10: # Conferindo notas de 10
        nota_10 += 1
        saque -= 10

    elif saque >= 1: # Conferindo notas de 1
        nota_1 += 1
        saque -= 1

print('--' * 15)
if nota_50 != 0:
    print(f'Total de {nota_50} cédulas de R$50')
if nota_20 != 0:
    print(f'Total de {nota_20} cédulas de R$20')
if nota_10 != 0:
    print(f'Total de {nota_10} cédulas de R$10')
if nota_1 != 0:
    print(f'Total de {nota_1} cédulas de R$1')
print('--' * 15)
print('Saque realizado. Volte sempre!')
