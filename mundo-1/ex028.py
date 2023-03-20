''' Escreva um programa que faça o computador “pensar” em um número inteiro entre 0 e 5
 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. 
 O programa deverá escrever na tela se o usuário venceu ou perdeu. '''

from random import randint
from time import sleep

print('-=' * 15)
print(' ' * 5, 'JOGO DA ADIVINHAÇÃO')
print('-=' * 15)

user = int(input('Digite um número de 0 a 5: '))
computador = randint(0, 5)
sleep(0.5)
print('-=' * 15)
print(f'Você: {user}')
print(f'Computador: {computador}')
print('-=' * 15)

if user == computador:
    print('Você venceu :)')
else: 
    print('Você perdeu :(')
