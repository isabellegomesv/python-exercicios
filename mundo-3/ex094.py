''' Crie um programa que leia nome, sexo e idade de várias pessoas,
guardando os dados de cada pessoa em um dicionário e todos os dicionários
em uma lista. No final, mostre:
A) Quantas pessoas foram cadastradas
B) A média de idade
C) Uma lista com as mulheres
D) Uma lista de pessoas com idade acima da média '''

dados = {}
pessoas = []
media = 0

while True:
    dados["nome"] = input('Nome: ').strip().title()
    dados["sexo"] = input('Sexo: [F/M] ').strip().upper()
    while dados["sexo"] not in 'FM':
        dados["sexo"] = input('Sexo: [F/M] ').upper()
    dados["idade"] = int(input('Idade: '))
    media += dados["idade"]
    pessoas.append(dados.copy())

    r = ' '
    while r not in 'SN':
        r = input('Quer continuar? [S/N] ').upper()
    if r == 'N':
        break

media /= len(pessoas)
print('=-' * 20)
print(f'No total foram cadastradas {len(pessoas)} pessoas.\n'
    f'A media de idade foi igual a {media:.2f} anos.')
print('Mulheres cadastradas: ',end='')
for p in range(len(pessoas)):
    if pessoas[p]["sexo"] == 'F':
        print(f'[{pessoas[p]["nome"]}]', end=' ')
    
print('\nPessoas acima da média de idade: ')
for p in range(len(pessoas)):
    if pessoas[p]["idade"] > media:
        print(f'Nome = {pessoas[p]["nome"]}'
        f' sexo = {pessoas[p]["sexo"]};'
        f' idade = {pessoas[p]["idade"]}')
print('=-' * 20)
print('ENCERRADO')
