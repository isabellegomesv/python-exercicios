''' Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas.
No final do programa, mostre: a média de idade do grupo, qual é o nome do
homem mais velho e quantas mulheres têm menos de 20 anos. '''

idades = 0
cont_sexom = 0
homem_velho = ''
maior = 0
tot_m = 0

for c in range(4):
    print('==' * 15)
    print(f'{"":^10}{c+1}ª PESSOA')
    print('==' * 15)
    nome = input('Digite o nome: ')
    idade = int(input('Digite a idade: '))
    sexo = input('Digite o sexo: [F/M] ').upper()
    idades += idade
    if sexo == 'M':
        cont_sexom += 1
        if cont_sexom == 1:
            maior = idade
            homem_velho = nome
        elif idade > maior:
            homem_velho = nome
            maior = idade
            
    elif sexo == 'F' and idade < 20:
        tot_m += 1

media_idade = idades / 4

print(f'Média de idade: {media_idade:.1f}.')
if homem_velho == '':
    print('Não há homens no grupo.')
else:
    print(f'O homem mais velho se chama {homem_velho}')
print(f'{tot_m} mulheres tem menos de 20 anos.')
