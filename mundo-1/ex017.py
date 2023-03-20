''' Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um 
triângulo retângulo. Calcule e mostre o comprimento da hipotenusa. '''

from math import hypot

print('=-=-' * 8)
print('Calculando Hipotenusa')
print('=-=-' * 8)

co = float(input('Cateto oposto: '))
ca = float(input('Cateto adjacente: '))
hipotenusa = hypot(co, ca)

print(f'h = {co}² + {ca}²\nh = {hipotenusa:.2f}')
