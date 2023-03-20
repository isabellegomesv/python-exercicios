''' Faça um mini-sistema que utilize o Interactive Help do Python. O usuário vai 
digitar o comando e o manual vai aparecer. Quando o usuário digitar a palavra 'FIM',
o programa se encerrará. Importante: use cores. '''

def ajuda(com):
    layout(f'Acessando o manual do comando \'{com}\'')
    print('\033[47m',end='')
    help(com)
    print('\033m')

def layout(msg):
    tamanho = len(msg) + 2
    print('\033[1;46m=\033[m' * tamanho)
    print(f'\033[1;39;42m {msg} \033[m')
    print('\033[1;46m=\033[m' * tamanho)



while True:
    layout('SISTEMA DE AJUDA PyHELP')
    resposta = input('Função ou Biblioteca: ').lower()
    if resposta != 'fim':
        ajuda(resposta)
    else:
        break
layout('ATÉ LOGO')
