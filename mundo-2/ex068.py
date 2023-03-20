''' Faça um programa que jogue par ou ímpar com o computador. 
O jogo só será interrompido quando o jogador perder, mostrando 
o total de vitórias consecutivas que ele conquistou no final do jogo. '''
from random import randint

print('=='* 15)
print(f'{"PAR OU ÍMPAR?":^30}')
print('=='* 15)

vitorias = 0

while True:
    n_user = int(input('Digite um número: '))
    pi_user = input('Par ou ímpar? [P/I] ').upper().strip()
    while pi_user not in 'PI':
        pi_user = input('Você digitou errado. '
                        'Tente novamente, par ou ímpar? [P/I] ').upper().strip()
    pc = randint(1, 10)
    pi = n_user + pc

    print('--'* 15)
    print(f'Você: {n_user}\n'
    f'Computador: {pc}\n'
    f'{f"Total = {pi}":^30}')
    print('--'* 15)
    if pi % 2 == 0:
        print(f'{"PAR!":^30}')
        print('--'* 15)
        if pi_user == 'P':
            print(f'{"Você ganhou!!":^30}')         
        else:
            break
    else:
        print(f'{"IMPAR":^30}')
        print('--'* 15)
        if pi_user == 'I':       
            print(f'{"Você ganhou!!":^30}')
        else:
            break
    print('--'* 15)
    vitorias += 1

print(f'GAME OVER! Você obteve o total de {vitorias} vitorias')
