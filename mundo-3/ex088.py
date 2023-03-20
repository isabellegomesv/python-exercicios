''' Faça um programa que ajude um jogador da MEGA SENA a criar palpites.
O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números 
entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta. '''

from random import randint
from time import sleep

print('=-' * 15)
print(f'{"PALPITES DA MEGA":^30}')
print('=-' * 15)
palpites = int(input('Quantos sorteios você deseja gerar? '))
sorteios = []
jogo = []
for c in range(palpites): # Palpites pedido
    for b in range(6): # Gerando um jogo de 6 números
        n = randint(1, 60)
        if n not in jogo: # Analisando se o nº está na lista para ñ se repetir
            jogo.append(n)
        else:
            while n in jogo:
                n = randint(1, 10)
            jogo.append(n)

    sorteios.append(jogo[:])
    jogo.clear()
print(f'{"=-=-= Sorteios gerados =-=-=":^30}')

for i, v in enumerate(sorteios):
    v.sort()
    print(f'Jogo {i+1}: {v}')
    sleep(0.5)
