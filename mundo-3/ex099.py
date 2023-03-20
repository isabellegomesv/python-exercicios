''' Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com 
valores inteiros. Seu programa tem que analisar todos os valores e dizer qual deles é o maior. '''
from time import sleep

def maior(*valores):
    print('-' * 30)
    cont = maior_num = 0
    for v in valores:
        print(f"{v}", end=' ', flush=True)
        sleep(0.25)

        # Descobrindo o maior número utilizando o laço for
        if cont == 0:
            maior_num = v
        else:
            if v > maior_num:
                maior_num = v

    print(f'Foram passados {len(valores)} valores.')
    maior_num = 0 

    
    print(f'O maior valor foi o {maior_num}.')
    '''
    # Utilizando o max()
    print(f'O maior valor foi o {max(valores)}.')
    '''


maior(2, 4, 1, 7)
maior(3, 1, 44, 2, 5)
maior(1, 2, 4)
