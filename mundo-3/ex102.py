''' Crie um programa que tenha uma função fatorial() que receba dois parâmetros: 
o primeiro que indique o número a calcular e outro chamado show, que será um valor 
lógico (opcional) indicando se será mostrado ou não na tela o processo de cálculo 
do fatorial. '''

def fatorial(n, show=False):
    '''
    Essa função serve para calcular o fatorial
    param n: número que vai ser fatorado
    param show: True para mostrar o calculo
    return: valor do fatorial de um número n
    '''
    if show:
        print(n, end=' x ')
    for cont in range(n - 1, 0, -1):
        if show:
            print(cont, end='')
            print(' x ' if cont > 1 else ' = ', end='')
        n *= cont
    return n


print(fatorial(5, show=True))
