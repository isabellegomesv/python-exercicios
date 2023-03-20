''' Desenvolva um programa que pergunte a distância de uma viagem em Km.
Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 
200Km e R$0,45 parta viagens mais longas. '''

print('==' * 15)
print(' ' * 8, 'Buss Company')
print('==' * 15)
km = int(input('Digite a distância da sua viagem em Km: '))

passagem = km * 0.50 if km <= 200 else km * 0.45

'''if km <= 200:
    passagem = km * 0.50
else:
    passagem = km * 0.45'''

print(f'O valor da passagem em uma viagem de {km}Km é de R${passagem:.2f}')
