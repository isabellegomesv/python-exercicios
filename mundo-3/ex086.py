''' Crie um programa que declare uma matriz de dimensão 3x3 e preencha com valores 
lidos pelo teclado. No final, mostre a matriz na tela, com a formatação correta. '''

matriz = [[], [], []]

for linha in range(len(matriz)):
    for coluna in range(3):
        n = int(input(f'Digite um número ({linha}, {coluna}): '))
        matriz[linha] += [n]

for linha in range(len(matriz)):
    for coluna in range(3):
        print(f'{f"[ {matriz[linha][coluna]:^5} ]"}', end='')
    print()
