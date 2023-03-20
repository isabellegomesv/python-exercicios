''' Escreva um programa que leia um número N inteiro qualquer e mostre na tela os 
N primeiros elementos de uma Sequência de Fibonacci. Exemplo:
0,1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584..
0 - 1 - 1 - 2 - 3 - 5 - 8 '''

print('==' * 15)
print(f'{"Sequência de Fibonacci":^30}')
print('==' * 15)

n = int(input('Quantos termos você quer mostrar: '))

# Para descobrir o proximo da sequência de fibonacci é preciso ter o ultimo e o penultimo número
penultimo = 0
ultimo = 1
c = 3
print(f'{penultimo} -> {ultimo}', end=' -> ')

while c <= n:  
    termo = ultimo + penultimo
    penultimo = ultimo
    ultimo = termo
    print(termo, end=' -> ')
    c += 1

print('FIM')
