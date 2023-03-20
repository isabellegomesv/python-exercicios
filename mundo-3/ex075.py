''' Desenvolva um programa que leia quatro valores pelo teclado e 
guarde-os em uma tupla. No final, mostre:

A) Quantas vezes apareceu o valor 9.
B) Em que posição foi digitado o primeiro valor 3.
C) Quais foram os números pares. '''

valores = (
    int(input('Digite o 1º número: ')), int(input('Digite o 2º número: ')),
    int(input('Digite o 3º número: ')), int(input('Digite o 4º número: ')),
)

print(f'Valores digitados: {valores}')

print(f'O número 9 apareceu {valores.count(9)} vezes')
print(f'O valor 3 está na posição {valores.index(3)}' 
    if valores.count(3) != 0 else 'Não tem o valor 3')

pares = False
for c in valores:
    if c % 2 == 0:
        pares = True

if pares:
    print('Os números pares foram: ', end='')
    for c in valores:
        if c % 2 == 0:
            print(c, end=' ')
else: 
    print('Não possui números pares.')
