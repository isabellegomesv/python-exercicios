''' Crie um programa onde o usuário possa digitar vários valores numéricos e 
cadastre-os em uma lista. Caso o número já exista lá dentro, ele não será adicionado. 
No final, serão exibidos todos os valores únicos digitados, em ordem crescente. '''

valores = []
while True:
    n = int(input('Digite um valor: '))
    if n in valores:
        print('Valor duplicado! Não vou adicionar.')
    else:
        valores += [n]
        print('Valor adicionado com sucesso!')
    r = ' '
    while r not in 'SN':
        r = input('Você quer continuar? [S/N] ').upper().strip()
    if r == 'N':
        break

print(f"Valores digitados em ordem crescente: {sorted(valores)}")
