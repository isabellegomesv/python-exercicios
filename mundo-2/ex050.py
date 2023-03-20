''' Desenvolva um programa que leia seis números inteiros e mostre a soma apenas
daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o. '''

soma = 0
contador = 0
for c in range(6):
    n = int(input(f'Digite o {c + 1}° número: '))
    if n % 2 == 0:
        soma += n
        contador += 1
print(f'A soma dos {contador} numeros pares é igual a {soma}')
