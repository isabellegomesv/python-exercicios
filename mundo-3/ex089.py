''' Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma 
lista composta. No final, mostre um boletim contendo a média de cada um e permita que o 
usuário possa mostrar as notas de cada aluno individualmente. '''

alunos = []
while True:
    # Pedindo dados do aluno:
    nome = input('Digite o nome do(a) aluno(a): ').strip().title()
    nota1 = float(input('Digite a 1º nota: '))
    nota2 = float(input('Digite a 2º nota: '))
    media = (nota1 + nota2) / 2 

    # Colocando dentro da lista:
    alunos.append([nome, [nota1, nota2], media])

    r = ' '
    while r not in 'SN':
        r = input('Você quer continuar? [S/N] ').upper()
    if r == 'N':
        break

# Mostrando os dados na tela de forma legivel
print(f'{"Nº":<5} {"Aluno":<10} {"Média":>11}')
print('--'*15)
for i, v in enumerate(alunos):
    print(f'{i:<5} {v[0]:<10} {v[2]:>10.1f}')
print('--'*15)

while True:
    n_aluno = int(input('Mostrar notas de qual aluno? [999 para interroper] '))
    if n_aluno == 999:
        break

    # Se o usuario digitar errado ou um número que não esteja na lista.
    if n_aluno < 0 or n_aluno > len(alunos) - 1:
        print('Número do aluno incorreto. Tente novamente!')
    else:
        print(f'Notas de {alunos[n_aluno][0]} são {alunos[n_aluno][1][0:]}')

print('Você saiu.')
