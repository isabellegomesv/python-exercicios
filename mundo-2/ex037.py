''' Escreva um programa em Python que leia um número inteiro qualquer e
peça para o usuário escolher qual será a base de conversão: 1 para binário,
2 para octal e 3 para hexadecimal. '''

print('=*' * 15)
print(' ' * 4, 'CONVERTOR DE NÚMEROS')
print('=*' * 15)

n = int(input('Digite um número: '))
base = int(input(
'''Escolha uma base de conversão:
[1] Binário
[2] Octal
[3] Hexadecimal
Digite: '''
))

if base == 1:
    binario = bin(n)
    print(f'{n} decimal = {binario[2:]} binário')

elif base == 2:
    octal = oct(n)
    print(f'{n} decimal = {octal[2:]} binário')

elif base == 3:
    hexa = hex(n)
    print(f'{n} decimal = {hexa[2:]} binário')

else:
    print('[ERRO] A opção selecionada não existe. Tente novamente!')
