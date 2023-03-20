''' Crie um programa que leia a idade e o sexo de várias pessoas. 
A cada pessoa cadastrada, o programa deverá perguntar se o usuário 
quer ou não continuar. No final, mostre:

A) quantas pessoas tem mais de 18 anos.
B) quantos homens foram cadastrados.
C) quantas mulheres tem menos de 20 anos. '''

pessoas_mais18 = 0
homens = 0
mulheres_menos20 = 0

while True:
    print('=-' * 15)
    print(f'{"CADASTRE UMA PESSOA":^30}')
    print('=-' * 15)
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'FM':
        sexo = input('Sexo: [M/F] ').upper().strip()
    
    if idade >= 18:
        pessoas_mais18 += 1
    elif idade < 20 and sexo == 'F':
        mulheres_menos20 += 1
    if sexo == 'M':
        homens += 1
    
    r = ' '
    while r not in 'SN':
        r = input('Deseja cadastrar mais uma pessoa? [S/N] ').upper().strip()
    if r == 'N':
        break

print('=-' * 15)
print(f'Cadastro finalizado.\n'
    f'Você cadastrou:\n'
    f'{pessoas_mais18} pessoas com mais de 18 anos de idade\n'
    f'{homens} homens\n'
    f'{mulheres_menos20} mulheres com menos de 20 anos de idade')
