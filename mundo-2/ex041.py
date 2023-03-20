''' A Confederação Nacional de Natação precisa de um programa que leia o
ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:

- Até 9 anos: MIRIM
- Até 14 anos: INFANTIL
- Até 19 anos: JÚNIOR
- Até 25 anos: SÊNIOR
- Acima de 25 anos: MASTER '''
from datetime import date

ano_nasc = int(input('Ano de nascimento: '))
ano_atual = date.today().year
idade = ano_atual - ano_nasc

if ano_nasc < ano_atual:
    if idade <= 9:
        print(f'Você tem {idade} anos e está na categoria MIRIM.')
    elif idade <= 14:
        print(f'Você tem {idade} anos e está na categoria INFANTIL.')
    elif idade <= 19:
        print(f'Você tem {idade} anos e está na categoria JUNIOR.')
    elif idade <= 25:
        print(f'Você tem {idade} anos e está na categoria SÊNIOR.')
    else:
        print(f'Você tem {idade} anos e está na categoria MASTER.')
else:
    print('\033[31m[ERRO] Impossivel verificar, o ano de nascimento é maior ou igual ao ano atual.'
    ' Tente Novamente!\033[m')
