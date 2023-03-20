''' Faça um programa que tenha uma função chamada área(), que receba as dimensões
de um terreno retangular (largura e comprimento) e mostre a área do terreno. '''

def firula(msg):
    print('-' * 30)
    print(' '* 5,msg)
    print('-' * 30)

def area(l, c):
    area_terreno = l * c
    print(f'A área de um terreno {l}x{c} é igual a {area_terreno}m².')

firula('Controle de Terrenos')
area(
    float(input('Digite a largura: (m) ')), 
    float(input('Digite o comprimento: (m) '))
)
