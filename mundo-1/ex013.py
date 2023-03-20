''' Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário,
com 15% de aumento. '''

salario_atual = float(input('Digite seu salário atual: R$'))
salario_novo = salario_atual + (salario_atual * 15 / 100)
print(f'O seu salário de R${salario_atual:.2f} recebeu um aumento de 15% e passara a ser ' 
    f'R${salario_novo:.2f}')
