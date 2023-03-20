''' Modifique as funções que form criadas no desafio 107 para que elas aceitem um parâmetro a mais, 
informando se o valor retornado por elas vai ser ou não formatado pela função moeda(), 
desenvolvida no desafio 108.'''

import moeda

n = float(input('Digite o preço: R$'))

print(f'Aumentando 10% temos R${moeda.aumentar(n, 10, True)}')
print(f'Diminuindo em 10% temos R${moeda.diminuir(n, 10, True)}')
print(f'O dobro de R${moeda.moeda(n)} é igual a R${moeda.dobro(n, True)}')
print(f'A metade de R${moeda.moeda(n)} é igual a R${moeda.metade(n, True)}')

