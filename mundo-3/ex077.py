''' Crie um programa que tenha uma tupla com várias palavras (não usar acentos). 
Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais. '''

palavras = (
    'amor', 'paz', 'cachorro', 'gato', 'feliz', 'triste',
    'programar', 'ler', 'estudar', 'passear', 'praticar'
    )

for palavra in palavras:
    print(f'Na palavra {palavra} temos: ', end='')
    for letra in palavra:
        if letra.lower() in 'aeiou':
            print(f'{letra}', end=' ')
    print()   
