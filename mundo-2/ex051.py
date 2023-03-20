''' Desenvolva um programa que leia o primeiro termo e a razão de uma PA.
No final, mostre os 10 primeiros termos dessa progressão. '''

a1 = int(input('Primeiro termo: '))
r = int(input('Razão: '))

# Formula para descobrir o ultimo número de uma PA
an = a1 + (10 - 1) * r
contador = 1
for c in range(a1, an+1, r):
    print(f"{contador}º: {c}")
    contador += 1
