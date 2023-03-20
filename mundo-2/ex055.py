''' Faça um programa que leia o peso de cinco pessoas. 
No final, mostre qual foi o maior e o menor peso lidos. '''

maior_peso = 0
menor_peso = 0

for c in range(5):
    peso = float(input(f'Digite o {c+1}ª peso: '))
    # Fazendo o primeiro peso ser maior e menor para conseguir comparar com os outros.
    if c == 1:
        maior_peso = peso
        menor_peso = peso

    # Comparando pesos para achar o maior e menor
    if peso > maior_peso:
        maior_peso = peso

    elif peso < menor_peso:
        menor_peso = peso

if maior_peso == menor_peso:
    print(f'O maior e menor peso foi igual a {maior_peso:.1f}kg')   
else:
    print(f'O maior peso foi: {maior_peso:.1f}Kg\nO menor peso foi: {menor_peso:.1f}Kg')
