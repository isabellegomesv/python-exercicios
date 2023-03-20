''' Crie um programa que faça o computador jogar Jokenpô com você. '''

import random
from time import sleep

print('VAMOS JOGAR JOKENPÔ')
user = input('Pedra, Papel ou Tesoura? ').strip().lower()
lista = ['pedra', 'papel', 'tesoura']
pc = random.choice(lista)
cores = {
    'verde': '\033[1;32m',
    'vermelho': '\033[1;31m',
    'limpa': '\033[m',
    'azul': '\033[36m'
}

print(' ', f'\033[1;42m JO {cores["limpa"]}')
sleep(0.5)
print(' ' * 6, f'\033[1;43m KEN {cores["limpa"]}')
sleep(0.5)
print(' ' * 12, f'\033[1;44m PÔ {cores["limpa"]}')
print('==' * 15)

print(f'{cores["azul"]}Você{cores["limpa"]}: {user}\n'
    f'{cores["azul"]}Computador{cores["limpa"]}: {pc}')
print('=='* 15)
sleep(0.5)

if user == pc:
    print('\033[33mEMPATE!\033[m')
elif user == 'pedra' and pc == 'papel':
    print(f'{cores["vermelho"]}Você perdeu!{cores["limpa"]} Papel embrulha pedra.') 
elif user == 'pedra' and pc == 'tesoura':
    print(f'{cores["verde"]}Você ganhou!!{cores["limpa"]} Pedra quebra teroura.')
elif user == 'papel' and pc == 'pedra':
    print(f'{cores["verde"]}Você ganhou!!{cores["limpa"]} Papel embrulha pedra.')
elif user == 'papel' and pc == 'tesoura':
    print(f'{cores["vermelho"]}Você perdeu!{cores["limpa"]} Tesoura corta papel.')
elif user == 'tesoura' and pc == 'papel':
    print(f'{cores["verde"]}Você ganhou!!{cores["limpa"]} Tesoura corta papel.')
elif user == 'tesoura' and pc == 'pedra':
    print(f'{cores["vermelho"]}Você perdeu!{cores["limpa"]} Pedra quebra tesoura.')
