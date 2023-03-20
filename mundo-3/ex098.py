''' Faça um programa que tenha uma função chamada contador(), que receba três parâmetros: 
início, fim e passo. Seu programa tem que realizar três contagens através da função criada:
a) de 1 até 10, de 1 em 1
b) de 10 até 0, de 2 em 2
c) uma contagem personalizada '''

from time import sleep

def contador(inicio, fim, passo):
    # Verificando se o passo é menor que 0 para deixa-lo positivo 
    if passo < 0:
        passo *= -1
    # Transformando passo 0 igual a 1
    elif passo == 0:
        passo = 1

    print('==' * 16)
    print(f'Contando de {inicio} até {fim} de {passo} em {passo}')
    if inicio < fim:
        for c in range(inicio, fim+1, passo):
            print(c, end=' ', flush=True)
            sleep(0.5)

    elif inicio > fim:
        for c in range(inicio, fim-1, -passo):
            print(c, end=' ', flush=True)
            sleep(0.5)

    print('FIM')
    print('==' * 16)


contador(1, 10, 1)
contador(10, 0, 2)
print('Agora é sua vez de personalizar a contagem!')
contador(
    inicio = int(input('Inicio: ')),
    fim = int(input('Fim: ')),
    passo = int(input('Passo: '))
)
