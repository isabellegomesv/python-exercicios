''' Faça um programa que leia nome e peso de várias pessoas,
guardando tudo em uma lista. No final, mostre:
A) Quantas pessoas foram cadastradas.
B) Uma listagem com as pessoas mais pesadas.
C) Uma listagem com as pessoas mais leves. '''

pessoas = list()
pessoa = list()
pesado = leve = 0
while True:
    # Cadastro da pessoa.
    pessoa.append(input('Nome: ').strip())
    pessoa.append(float(input('Peso: ')))

    if len(pessoas) == 0: # Analisando pessoas leves e pesadas
        pesado = pessoa[1]
        leve = pessoa[1]

    else:
        if pessoa[1] > pesado:
            pesado = pessoa[1]
        if pessoa[1] < leve:
            leve = pessoa[1]
    pessoas.append(pessoa[:]) # Juntando
    pessoa.clear() 

    r = ' '
    while r not in 'SN':
        r = input('Quer continuar? [S/N] ').upper()
    if r  == 'N':
        break

print(f'Foram cadastrados {len(pessoas)} pessoas.')

print(f'Pessoa(s) mais pesada(s) com {pesado}Kg: ', end='')
for c in range(len(pessoas)):
    if pessoas[c][1] == pesado:
        print(f'[{pessoas[c][0]}]', end=' ')

print(f'\nPessoa(s) mais leve(s) com {leve}Kg: ', end='')
for c in range(len(pessoas)):
    if pessoas[c][1] == leve:
        print(f'[{pessoas[c][0]}]', end=' ')
