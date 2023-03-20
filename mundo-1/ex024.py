''' Crie um programa que leia o nome de uma cidade diga 
se ela começa ou não com o nome “SANTO”. '''

cidade = str(input('Digite o nome de uma cidade: ')).strip().lower()
separa = cidade.split()
verifica = 'santo' in separa[0]

print(f'Essa frase começa com Santo?: {verifica}')
