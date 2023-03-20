''' Crie um programa que leia o ano de nascimento de sete pessoas.
No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores. '''
import datetime

ano_atual = datetime.date.today().year
menor_idade = 0
maior_idade = 0 
for c in range(1, 7+1):
    ano_nasc = int(input(f'Digite o {c}° ano de nascimento: '))
    idade = ano_atual - ano_nasc
    if idade < 18:
        menor_idade += 1
    else:
        maior_idade += 1

print(f'Nesse grupo de pessoas {menor_idade} são menor de idade e '
    f'{maior_idade} são maiores de idade.')
