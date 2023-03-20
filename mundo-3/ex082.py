''' Crie um programa que vai ler vários números e colocar em uma lista. 
Depois disso, crie duas listas extras que vão conter apenas os valores pares 
e os valores ímpares digitados, respectivamente. Ao final, mostre o conteúdo 
das três listas geradas. '''

lista = []
par = []
impar = []

# Opção 1
while True: 
    n = int(input('Digite um número: '))
    if n % 2 == 0:
        par.append(n)
    else:
        impar.append(n)
    lista.append(n)
    r = ' '
    while r not in 'SN':
        r = input('Quer continuar? [S/N] ').upper()
    if r == 'N':
        break

# Opção 2
'''while True: 
    lista.append(int(input('Digite um número: ')))
    r = ' '
    while r not in 'SN':
        r = input('Quer continuar? [S/N] ').upper()
    if r == 'N':
        break

for i, v in enumerate(lista):
    if v % 2 == 0:
        par.append(v)
    else:
        impar.append(v)'''

print(f'Valores digitados: {lista}')
print(f'Pares: {par}' if len(par) > 0 else 'Não há números par na lista')
print(f'Impares: {impar}' if len(impar) > 0 else 'Não há números impar na lista')
