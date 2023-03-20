''' Desenvolva um programa que leia o comprimento de três retas e
diga ao usuário se elas podem ou não formar um triângulo. 

#IMPORTANTE: Para formar um triângulo, a soma de cada dois lados deve ser sempre
maior que a medida do terceiro lado.'''

cores = {
    'rosaverde': '\033[1;32;45m',
    'verde': '\033[4;32m',
    'vermelho': '\033[4;31m',
    'limpa': '\033[m'
}
print(f'{cores["rosaverde"]}^^\033[m' * 15)
print('Analisador de Triângulos')
print(f'{cores["rosaverde"]}^^\033[m' * 15)

a = float(input('Primeiro comprimento: '))
b = float(input('Segundo comprimento: '))
c = float(input('Terceiro comprimento: '))

if a + b > c and a + c > b and b + c > a:
    print(f'{cores["verde"]}Pode formar um triângulo.{cores["limpa"]}')
else:
    print(f'{cores["vermelho"]}Não pode formar um triângulo.{cores["limpa"]}')
