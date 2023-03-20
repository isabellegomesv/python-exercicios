''' Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. 
Guarde esses resultados em um dicionário em Python. No final, coloque esse dicionário em ordem, 
sabendo que o vencedor tirou o maior número no dado. '''

from random import randint
from time import sleep

print('==' * 15)
print(f'{"JOGO DOS DADOS":^30}')
print('==' * 15)

jogadores = {}

for c in range(4):
    jogadores[f'jogador{c+1}'] = randint(1, 6)

for k, v in jogadores.items():
    print(f'{f"{k} tirou {v} no dado":^30}')
    sleep(0.5)
print('--' * 15)

ranking = sorted(jogadores.items(), key=lambda x:x[1], reverse=True)

pos = 1
for k,v in ranking:
    print(f'{k} ficou em {pos}º tirando {v}')
    pos += 1
