''' Faça um programa que leia um ângulo qualquer e mostre na 
tela o valor do seno, cosseno e tangente desse ângulo. '''

from math import radians, sin, cos, tan

angulo = int(input('Digite um ângulo: '))
seno = sin(radians(angulo))
cosseno = cos(radians(angulo))
tangente = tan(radians(angulo))

print(f'O ângulo de {angulo}° corresponde a:\n'
    f'Seno: {seno:.2f}\n'
    f'Cosseno: {cosseno:.2f}\n'
    f'Tangente: {tangente:.2f}\n')
