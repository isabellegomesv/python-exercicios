''' Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla. 
Depois disso, mostre a listagem de números gerados e também indique o menor e o 
maior valor que estão na tupla. '''

from random import randint
n = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))
print(f'Tupla sorteada: {n}\n'
    f'Maior número: {max(n)}\n'
    f'Menor número: {min(n)}')
