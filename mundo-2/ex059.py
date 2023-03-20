''' Crie um programa que leia dois valores e mostre um menu na tela:

[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa

Seu programa deverá realizar a operação solicitada em cada caso. '''

from time import sleep

n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor: '))
menu = 0
cores = {
    'amarelo' : '\033[33m',
    'vermelho' : '\033[31m',
    'limpa' : '\033[m',
    'cinza' : '\033[30m'
}
while menu != 5:
    sleep(0.5)
    print('==' * 15)
    print(f'{"MENU":^30}')
    print('=='* 15)
    menu = int(input('[ 1 ] Somar\n'
    '[ 2 ] Multiplicar\n'
    '[ 3 ] Maior\n'
    '[ 4 ] Novos números\n'
    '[ 5 ] Sair do programa\n' 
    'Escolha uma opção: '))
    print('=='* 15)
    if menu == 1:
        soma = n1 + n2
        print(f'{cores["amarelo"]}O resultado de {n1} + {n2} é igual a {soma}.{cores["limpa"]}')
    elif menu == 2:
        mult = n1 * n2
        print(f'{cores["amarelo"]}O resultado de {n1} x {n2} é igual a {mult}{cores["limpa"]}')
    elif menu == 3:
        if n1 > n2:
            print(f'{cores["amarelo"]}{n1} é maior que {n2}{cores["limpa"]}')
        elif n2 > n1:
            print(f'{cores["amarelo"]}{n2} é maior que {n1}{cores["limpa"]}')
        else:
            print(f'{cores["amarelo"]}Os números são iguais!{cores["limpa"]}')
    elif menu == 4:
        n1 = int(input('Digite outro valor: '))
        n2 = int(input('Digite outro valor: '))
    elif menu == 5:
        pass
    else:
        print(f'{cores["vermelho"]}Opção inválida. Tente novamente!{cores["limpa"]}')

print(f'{cores["cinza"]}Você saiu.{cores["limpa"]}')
