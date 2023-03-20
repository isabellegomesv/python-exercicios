''' Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
Para salários superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais,
o aumento é de 15%. '''

salario = float(input('Digite seu salário: '))

if salario <= 1250:
    salario_novo = salario + (salario * 15 / 100)
    print(f'Você recebeu um aumento de 15%, agora seu salário sera de R${salario_novo:.2f}')

else:
    salario_novo = salario + (salario * 10 / 100 )
    print(f'Você recebeu um aumento de 10%, agora seu salário sera de R${salario_novo:.2f}')
