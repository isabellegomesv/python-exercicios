''' Aprimore o desafio 93 para que ele funcione com vários jogadores, 
incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador. '''

jogadores = []
dados_jogador = {}
gols = []

# Pedindo dados dos jogadores ao usuario
while True:
    dados_jogador['nome'] = input('Nome do jogador: ').strip().title()
    partidas = int(input(f'Quantas partidas {dados_jogador["nome"]} jogou? '))
    for partida in range(partidas):
        gols.append(int(input(f'Quantos gols na partida {partida+1}? ')))
    dados_jogador['gols'] = gols[:]
    gols.clear()
    dados_jogador['total'] = sum(dados_jogador['gols'])
    jogadores.append(dados_jogador.copy())

    r = ' '
    while r not in 'SN':
        r = input('Quer continuar? [S/N] ').upper().strip()
    if r == 'N':
        break

# Tabela com dados do jogador
print('--' * 20)
print(f'{"Nº":<5} {"Nome":<15} {"Gols":<8} {"Total":>8}')
print('--' * 20)
for k, v in enumerate(jogadores):
    print(f'{k:<5} ', end='')
    for d in v.values():
        print(f'{str(d):<15}',end='')
    print()
print('--' * 20)

# Mostrar dados do jogador para o usuario
while True:
    mostrar_dados = int(input('Mostrar dados de qual jogador? [999 para sair] '))
    if mostrar_dados == 999:
        break
    if mostrar_dados < 0 or mostrar_dados > len(jogadores) - 1:
        print('Jogador não encontrado. Tente novamente!')
    else:
        print(f' --Levantamento do jogador {jogadores[mostrar_dados]["nome"]}')
        for k, v in enumerate(jogadores[mostrar_dados]["gols"]):
            print(f'No jogo {k+1} fez {v} gols.')
        print('--' * 20)

print('--- Volte sempre! ---')
