''' Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h,
mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada Km 
acima do limite. '''

print('*-' * 15)
print(' ' * 5, 'Radar Eletrônico')
print('*-' * 15)
vel = int(input('Velocida do carro: '))

if vel > 80:
    multa = (vel - 80) * 7
    print(f'MULTADO! Você ultrapassou o limite da pista e terá que pagar a multa de R${multa:.2f}!')
else:
    print('Velocidade dentro do limite!')
print('Tenha um bom dia! Dirija com segurança!')
