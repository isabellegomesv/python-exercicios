''' Crie um programa que leia o nome de uma pessoa e diga se ela tem “SILVA” no nome '''

nome = input('Digite seu nome: ').strip().upper()
verifica = 'SILVA' in nome.split()
print(f'O seu nome tem Silva? {verifica}')
