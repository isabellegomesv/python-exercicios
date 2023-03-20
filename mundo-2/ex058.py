''' Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número entre 0 e 10. 
Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos 
palpites foram necessários para vencer. '''

from random import randint

print('-=' * 17)
print(' ' * 5, 'JOGO DA ADIVINHAÇÃO v2.0')
print('-=' * 17)

user = int(input('Em que número estou pensando? [0, 10] '))
computador = randint(0, 10)
palpites = 0

while user != computador:
    user = int(input('ERROU! Tente adivinhar novamente: '))
    palpites += 1
    if user > computador:
        print('Menos... Tente mais uma vez!')
    elif user < computador:
        print('Mais... Tente mais uma vez!')

print('-=' * 17)
print(f'Você: {user}')
print(f'Computador: {computador}')
print('-=' * 17)
print(f'Parabéns!! Você conseguiu adivinhar com {palpites} palpite(s)')
