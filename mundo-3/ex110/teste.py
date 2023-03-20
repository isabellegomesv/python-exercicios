''' Modifique as funções que form criadas no desafio 107 para que elas aceitem um parâmetro a mais, 
informando se o valor retornado por elas vai ser ou não formatado pela função moeda(), 
desenvolvida no desafio 108.'''

import moeda

n = float(input('Digite o preço: R$'))
moeda.resumo(n, 10, 10)
