''' Faça um programa que leia o nome completo de uma pessoa,
mostrando em seguida o primeiro e o último nome separadamente. '''

nome = input('Digite seu nome: ').title().strip().split()
primeiro_nome = nome[0]
ultimo_nome = nome[-1]

print(f'Seu primeiro nome é {primeiro_nome}\nSeu ultimo nome é {ultimo_nome}')
