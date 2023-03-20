'''  Crie um programa onde o usuário possa digitar sete valores numéricos e 
cadastre-os em uma lista única que mantenha separados os valores pares e ímpares. 
No final, mostre os valores pares e ímpares em ordem crescente. '''

lista = [[], []]

for c in range(7):
    n = int(input('Digite um número: '))
    if n % 2 == 0:
        lista[0] += [n]
    else:
        lista[1] += [n]

lista[0].sort()
lista[1].sort()
print(f'Os valores pares: {lista[0]}\n'
    f'Os valores impares: {lista[1]}')
