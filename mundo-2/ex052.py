''' Faça um programa que leia um número inteiro e diga se ele é ou não um número primo. '''

print('IDENTIFICADOR DE NÚMEROS PRIMOS')
n = int(input('Digite um número: '))
total = 0 
for c in range(1, n+1):
    if n % c == 0:
        print('\033[34m', end='')
        total += 1
    else:
        print('\033[m', end='')
    print(f'{c}', end=' ')

print(f'\033[m\nO número {n} foi divisivel {total} vezes.')
if total <= 2:
    print('É um número primo.')
else:
    print('Não é um número primo.')
