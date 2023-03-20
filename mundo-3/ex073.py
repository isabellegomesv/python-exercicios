''' Crie uma tupla preenchida com os 20 primeiros colocados da 
Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:

a) Os 5 primeiros times.
b) Os últimos 4 colocados.
c) Times em ordem alfabética.'''

times = (
    'Palmeiras', 'Internacional', 'Fluminense', 'Corinthians', 'Flamengo',
    'Athletico-PR', 'Atlético-MG', 'Fortaleza', 'São Paulo', 'America-MG',
    'Botafogo', 'Santos', 'Goias', 'Bragantino', 'Coritiba',
    'Cuiaba', 'Ceara SC', 'Atletico-GO', 'Avaí', 'Juventude', 
)

print('Os primeiros colocados: ')
for c in range(5):
    print(f'{c+1}º: {times[c]}', end='')
    if c == 4:
        print(end='')
    else:
        print(end=', ')

print('\nUltimos colocados: ')
pos = 17
for c in range(4, 0, -1):
    print(f'{pos}º: {times[-c]}', end='')
    if c == 1:
        print(end='')
    else:
        print(end=', ')
    pos += 1

print('\nEm ordem afabética: ')

for c in sorted(times):
    print(c, end=', ')
