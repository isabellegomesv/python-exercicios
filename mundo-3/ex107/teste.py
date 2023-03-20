'''Crie um módulo chamado moeda.py que tenha as funções incorporadas aumentar(), 
diminuir(), dobro() e metade(). Faça também um programa que importe esse 
módulo e use algumas dessas funções.'''

import moeda

n = int(input('Digite o preço: '))

print(f'Aumentando 10% temos R${moeda.aumentar(n, 10):.2f}')
print(f'Diminuindo em 10% temos R${moeda.diminuir(n, 10):.2f}')
print(f'O dobro de R${n:.2f} é igual a R${moeda.dobro(n):.2f}')
print(f'A metade de R${n:.2f} é igual a R${moeda.metade(n):.2f}')
