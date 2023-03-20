''' Refaça o DESAFIO 51, lendo o primeiro termo e a razão de uma PA, 
mostrando os 10 primeiros termos da progressão usando a estrutura while. '''

a1 = int(input('Primeiro termo: '))
r = int(input('Razão: '))

contador = 1

while contador <= 10:
    print(f'{contador}º = {a1}')
    a1 += r
    contador += 1
