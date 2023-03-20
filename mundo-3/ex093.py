'''Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa 
vai ler o nome do jogador e quantas partidas ele jogou. Depois vai ler a quantidade de 
gols feitos em cada partida. No final, tudo isso será guardado em um dicionário, incluindo
o total de gols feitos durante o campeonato.'''

dados_jogador = {}
gols = []
dados_jogador['nome'] = input('Nome do jogador: ').strip().title()
partidas = int(input(f'Quantas partidas {dados_jogador["nome"]} jogou? '))

for partida in range(partidas):
    gols.append(int(input(f'Quantos gols na partida {partida+1}? ')))

dados_jogador['gols'] = gols[:]
dados_jogador['total'] = sum(dados_jogador['gols'])

print('=-' * 20)
print(dados_jogador)
print('=-' * 20)
for k, v in dados_jogador.items():
    print(f'O campo {k} tem o valor {v}')
print('=-' * 20)

print(f'O jogador {dados_jogador["nome"]} jogou {partidas} partidas.')
for partida, gol in enumerate(dados_jogador['gols']):
    print(f'Na partida {partida+1} fez {gol} gols.')

print(f'Foi um total de {dados_jogador["total"]} gols.')
