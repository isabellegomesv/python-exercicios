''' Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. 
No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas 
posições na lista. '''

valores = []
maior = 0 
menor = 0
for c in range(5):
    valores.append(int(input(f"Digite o {c+1}º número: ")))
    if c == 0:
        maior = menor = valores[c]
    else:
        if valores[c] > maior :
            maior = valores[c]
        if valores[c] < menor:
            menor = valores[c]

print(f'Números digitados: {valores}')
print(f'Maior valor: {maior} na posição: ', end='')
for i, v in enumerate(valores):
    if v == maior:
        print(f'{i}', end='...')

print(f'\nMenor valor: {menor} na posição:  ', end='')
for i, v in enumerate(valores):
    if v == menor:
        print(f'{i}', end='...')
