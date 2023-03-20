''' Faça um programa que leia um número de 0 a 9999 e mostre na tela 
cada um dos dígitos separados. '''

n = int(input('Digite um número: '))

u = n // 1 % 100
d = n // 10 % 10
c = n // 100 % 10
m = n // 1000 % 10
print(f'Analisando o número {n}\n'
    f'Unidade: {u}\n'
    f'Dezena: {d}\n'
    f'Centena: {c}\n'
    f'Milhar: {m}')
