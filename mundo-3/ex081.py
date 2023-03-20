''' Crie um programa que vai ler vários números e colocar em uma lista.
Depois disso, mostre:
A) Quantos números foram digitados.
B) A lista de valores, ordenada de forma decrescente.
C) Se o valor 5 foi digitado e está ou não na lista. '''

lista = []

while True:
    lista.append(int(input('Digite um número: ')))
    r = ' '
    while r not in 'SN':
        r = input('Você quer continuar? [S/N] ').upper()
    if r == 'N':
        break

lista.sort(reverse=True)
print(f'Foram digitados {len(lista)} valores: {lista}\n'
    'O número 5 está na lista' if lista.count(5) >= 1 else 'O número 5 não está na lista')
