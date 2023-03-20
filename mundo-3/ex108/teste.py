'''Adapte o código do desafio #107, criando uma função adicional chamada moeda() 
que consiga mostrar os números como um valor monetário formatado.'''

import moeda

n = float(input('Digite o preço: R$'))

print(f'Aumentando 10% temos R${moeda.moeda(moeda.aumentar(n, 10))}')
print(f'Diminuindo em 10% temos R${moeda.moeda(moeda.diminuir(n, 10))}')
print(f'O dobro de R${moeda.moeda(n)} é igual a R${moeda.moeda(moeda.dobro(n))}')
print(f'A metade de R${moeda.moeda(n)} é igual a R${moeda.moeda(moeda.metade(n))}')
