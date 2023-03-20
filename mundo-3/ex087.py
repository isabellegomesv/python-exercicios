''' Aprimore o desafio anterior, mostrando no final:
A) A soma de todos os valores pares digitados.
B) A soma dos valores da terceira coluna.
C) O maior valor da segunda linha. '''

matriz = [[], [], []]
pares = 0
soma_terceira_coluna = 0

for linha in range(len(matriz)):
    for coluna in range(3):
        n = int(input(f'Digite um número ({linha}, {coluna}): '))
        if n % 2 == 0:
            pares += n
        matriz[linha] += [n]

for linha in range(len(matriz)):
    for coluna in range(3):
        print(f'{f"[ {matriz[linha][coluna]:^5} ]"}', end='')
    print()

for linha in matriz:
    soma_terceira_coluna += linha[2]

print(f'Soma dos números pares: {pares}')
print(f'Soma dos números da terceira coluna: {soma_terceira_coluna}')
print(f'Maior valor da segunda linha: {max(matriz[1])}')
