''' Faça um programa que leia o ano de nascimento de um jovem e informe,
de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar,
se é a hora exata de se alistar ou se já passou do tempo do alistamento.
Seu programa também deverá mostrar o tempo que falta ou que passou do prazo '''

import datetime
ano_nasc = int(input('Digite o ano em que você nasceu: '))
ano_atual = datetime.date.today().year
idade = ano_atual - ano_nasc

if idade > 18:
    print(f'Não é mais obrigatorio, você deve ter se alistado a {idade - 18} anos atras.')
elif idade == 18:
    print('Você tem que se alistar agora!')
else:
    print(f'Ainda faltam {18 - idade} anos para você se alistar.')
