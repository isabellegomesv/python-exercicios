''' Faça um programa que leia três números e mostre qual é o maior e qual é o menor. '''

num_1 = int(input('Digite o 1º número: '))
num_2 = int(input('Digite o 2º número: '))
num_3 = int(input('Digite o 3º número: '))

maior = num_1
menor = num_1

# Maior número
if num_2 > num_1 and num_2 > num_3:
    maior = num_2

if num_3 > num_2 and num_3 > num_1:
    maior = num_3

# Menor número
if num_2 < num_1 and num_2 < num_3:
    menor = num_2

if num_3 < num_2 and num_3 < num_1:
    menor = num_3

if menor == maior:
    print('Todos os números são iguais!')
else:
    print(f"O maior número é o {maior} e o menor é o {menor}")
