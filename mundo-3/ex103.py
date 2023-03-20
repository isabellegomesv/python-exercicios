''' Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros 
opcionais: o nome de um jogador e quantos gols ele marcou. O programa deverá ser capaz 
de mostrar a ficha do jogador, mesmo que algum dado não tenha sido informado corretamente. '''

def ficha(jogador='<desconhecido>', gol=0):
    return f'O jogador {jogador} fez {gol} gol(s) no campeonato.'


jog = input('Nome do jogador: ')
g =input('Número de gol(s): ')
if g.isnumeric():
    g = int(g)
else:
    g = 0
if jog.strip() == '':
    print(ficha(gol=g))
else:
    print(ficha(jog, g))


