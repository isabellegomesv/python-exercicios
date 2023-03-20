''' Faça um programa que mostre a tabuada de vários números, um de cada vez, 
para cada valor digitado pelo usuário. O programa será interrompido quando o 
número solicitado for negativo. '''
c = 1
while True:
    tabuada = int(input('Digite um número para ver sua tabuada: '))
    if tabuada < 0:
        break
    for c in range(1, 11):
        print(f'{c} x {tabuada} = {c * tabuada}')

print('Programa encerrado.')