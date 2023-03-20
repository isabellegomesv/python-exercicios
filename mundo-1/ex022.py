'''Crie um programa que leia o nome completo de uma pessoa e mostre:

- O nome com todas as letras maiúsculas e minúsculas.

- Quantas letras ao todo (sem considerar espaços).

- Quantas letras tem o primeiro nome.'''

nome = input('Digite seu nome completo: ').strip()
dividido = nome.split()
completo = ''.join(dividido)

print(f'O seu nome completo é {nome}\n'
    f'Em maiúsculas: {nome.upper()}\n'
    f'Em minúscula: {nome.lower()}\n'
    f'Possui o total de {len(completo)} letras\n'
    f'O primeiro nome tem o total de {len(dividido[0])}')
