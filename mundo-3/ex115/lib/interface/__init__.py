def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[31m[ERRO] Digite um número inteiro válido!\033[m')
        else:
            return n

def linhas():
    print('-' * 40)

def head(msg):
    linhas()
    print(f'{msg:^40}')
    linhas()

def menu(lst):
    head('MENU PRINCIPAL')
    c = 1
    for i in lst:
        print(f'\033[33m{c}\033[m - \033[36m{i}\033[m')
        c += 1
    linhas()
    opcao = leiaInt('Sua opção: ')
    return opcao
