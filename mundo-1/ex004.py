''' Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo
e todas as informações possíveis sobre ele.'''

a = str(input('Digite algo: '))
print(f'O tipo primitivo desse valor é {type(a)}')
print(f'So tem espaços? {a.isspace()}')
print(f'É um número? {a.isnumeric()}')
print(f'É alfabético? {a.isalpha()}')
print(f'É alphanumérico? {a.isalnum()}')
print(f'Está em maiúsculas? {a.isupper()}')
print(f'Está minúscula? {a.islower()}')
print(f'Está capitalizada? {a.istitle()}')
