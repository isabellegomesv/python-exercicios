''' Faça um programa que leia um número qualquer e mostre o seu fatorial. Exemplo:
5! = 5 x 4 x 3 x 2 x 1 = 120 '''

fatorial = int(input('Digite um número para calcular o fatorial: '))
c = fatorial - 1
print(f'{fatorial}! = {fatorial} x ', end='')
while c != 0:
    print(f'{c}', end='')
    print(' x ' if c > 1 else ' = ', end='')
    fatorial *= c
    c -= 1

'''
# Utilizando o laço for
for c in range(fatorial - 1, 0, -1): 
    print(f'{c}', end='')
    print(' x ' if c > 1 else ' = ', end='')
    fatorial *= c'''
print(fatorial)
