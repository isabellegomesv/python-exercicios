''' Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por 
extenso, de zero até vinte. Seu programa deverá ler um número pelo teclado (entre 0 e 20) 
e mostrá-lo por extenso. '''

numeros_extenso = (
    'zero', 'um', 'dois', 'três', 'quatro', 'cinco', 
    'seis', 'sete', 'oito', 'nove', 'dez',
    'onze', 'doze', 'treze', 'quatorze', 'quinze',
    'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte'
)

n = int(input('Digite um número de 0 a 20: '))

while n > 20 or n < 0:
    n = int(input('Número inválido! Digite um número de 0 a 20: '))

print(f'O número {n} por extenso é igual a {numeros_extenso[n]}')
