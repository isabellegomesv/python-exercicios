''' Faça um programa que tenha uma lista chamada números e duas funções chamadas 
sorteia() e somaPar(). A primeira função vai sortear 5 números e vai colocá-los 
dentro da lista e a segunda função vai mostrar a soma entre todos os valores pares 
sorteados pela função anterior. '''

from random import randint
from time import sleep

def sorteio(lst):
    print('Sorteando números: ',end='')
    for c in range(5):
        n = randint(0, 10)
        print(n, end=' ', flush=True)
        sleep(0.3)
        lst.append(n)
    print()


def somaPar(lst):
    soma = 0
    print('Números pares na lista: ',end='')
    for c in lst:
        if c % 2 == 0:
            print(f'[{c}]', end=' ', flush=True)
            sleep(0.3)
            soma += c
    print(f'\nSoma dos números pares é igual {soma}')

    
numeros = []
sorteio(numeros)
somaPar(numeros)
