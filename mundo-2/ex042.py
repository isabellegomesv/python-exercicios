''' Refaça o DESAFIO 35 dos triângulos, acrescentando o recurso
de mostrar que tipo de triângulo será formado:

- EQUILÁTERO: todos os lados iguais
- ISÓSCELES: dois lados iguais, um diferente
- ESCALENO: todos os lados diferentes '''

print('-*' * 15)
print(' ' * 2,'Analisador de Triângulos')
print('-*' * 15)

a = float(input('Primeiro comprimento: '))
b = float(input('Segundo comprimento: '))
c = float(input('Terceiro comprimento: '))

if a + b > c and a + c > b and b + c > a:
    print('Os seguimentos podem formar um triângulo', end=' ')
    if c == a == b:
        print('EQUILÁTERO!')
    elif a == b != c or b == c != a or c == a != b:
        print('ISÓSCELES!')
    else:
        print('ESCALENO!')
else:
    print('Não pode formar um triângulo.')
