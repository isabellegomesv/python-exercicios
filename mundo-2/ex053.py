''' Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo,
desconsiderando os espaços. Exemplos de palíndromos:

APOS A SOPA, A SACADA DA CASA, A TORRE DA DERROTA, O LOBO AMA O BOLO,
ANOTARAM A DATA DA MARATONA. '''

frase = input('Digite uma frase: ').upper()
frase_junta = frase.replace(' ', '')
frase_reverso = frase_junta[::-1]
print(f'Frase invertida: {frase_reverso}')
if frase_junta == frase_reverso:
    print('Esta frase é um palíndromo.')
else:
    print('Esta frase não é um palíndromo.')
