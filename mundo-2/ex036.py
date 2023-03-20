''' Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado. '''

print('\033[33;44m-=-\033[m'* 15)
print(' ' * 10,'\033[33mBANCO ITAISA - EMPRESTIMOS\033[33m')
print('\033[33;44m-=-\033[m'* 15)

valor_casa = float(input('\033[1;30mValor da casa: R$'))
salario = float(input('Seu salário: R$'))
anos_pagamento = int(input('Em quantos anos você deseja pagar? '))

prestacao = valor_casa / (anos_pagamento * 12)
salario_30 = salario * 30 / 100

if prestacao > salario_30:
    print(f'\033[m\033[1;31mEmprestimo negado!\033[m '
    f'A prestação R${prestacao:.2f} excedeu 30% do seu salário.')
else:
    print(f'\033[1;32mEmprestimo aprovado!\033[m A sua prestação será de R${prestacao:.2f}')
