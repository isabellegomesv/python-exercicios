''' Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'. 
Caso esteja errado, peça a digitação novamente até ter um valor correto. '''

sexo = input('Informe o seu sexo: [M/F] ')

while sexo not in 'MmFf':
    sexo = input('Dados incorretos! Por favor, informe seu sexo: ')

if sexo in 'Mm':
    print('Sexo masculino registrado com sucesso!')
else:
    print('Sexo feminino registrado com sucesso!')

''' 
# Outra Solucão:

while 'm' != sexo != 'f':
    sexo = input('Dados incorretos! Por favor, informe seu sexo: ')
'''
