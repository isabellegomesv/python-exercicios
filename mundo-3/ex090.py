''' Faça um programa que leia nome e média de um aluno, guardando também a situação
 em um dicionário. No final, mostre o conteúdo da estrutura na tela. '''

aluno = {}
aluno['nome'] = input('Nome do aluno: ').strip().title()
aluno['media'] = float(input(f'Media de {aluno["nome"]}: '))

if aluno['media'] <= 5:
    aluno['situaçao'] = 'Reprovado'
elif aluno['media'] < 7:
    aluno['situaçao'] = 'Recuperação'
else:
    aluno['situaçao'] = 'Aprovado'

print('--' * 15)
for k, v in aluno.items():
    print(f'{k} é igual a {v}')
