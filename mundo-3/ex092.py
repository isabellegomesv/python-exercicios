''' Crie um programa que leia nome, ano de nascimento e carteira de trabalho e 
cadastre-o (com idade) em um dicionário. Se por acaso a CTPS for diferente de ZERO, 
o dicionário receberá também o ano de contratação e o salário. Calcule e acrescente, 
além da idade, com quantos anos a pessoa vai se aposentar '''

import datetime

pessoa = {}
ano_atual = datetime.date.today().year
pessoa['nome'] = input('Nome: ').title().strip()
ano_nasc = int(input('Ano de Nascimento: '))
pessoa['idade'] = ano_atual - ano_nasc
pessoa['ctps'] = int(input('Carteira de trabalho: (0 não tem) '))
if pessoa['ctps'] != 0:
    pessoa['contratação'] = int(input('Ano de contratação: '))
    pessoa['aposentadoria'] = (pessoa['contratação'] + 35) - ano_atual
print('-='*15)
for k, v in pessoa.items():
    print(f' - {k} tem o valor {v}')
