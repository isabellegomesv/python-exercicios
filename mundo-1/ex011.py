'''Faça um programa que leia a largura e a altura de uma parede em metros, 
calcule a sua área e a quantidade de tinta necessária para pintá-la, 
sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.'''

print('-='* 10)
print('Calculadora de tinta')
print('-='* 10)

largura = float(input('Largura da parede em metros: '))
altura = float(input('Altura da parede em metros: '))
area = altura * largura
tinta = area / 2
print(f'A sua parede tem {area}m² e gastaria o total de {tinta}L de tinta para pintar.')
