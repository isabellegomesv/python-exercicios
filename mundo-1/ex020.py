''' O mesmo professor do desafio 19 quer sortear a ordem de apresentação de trabalhos dos alunos.
Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada. '''

from random import shuffle

aluno1 = input('Primeiro Aluno: ')
aluno2 = input('Segundo Aluno: ')
aluno3 = input('Terceiro Aluno: ')
aluno4 = input('Quarto Aluno: ')

lista = [aluno1, aluno2, aluno3, aluno4]
shuffle(lista)
print(f'A ordem de aprensentação será: {lista}')
# print(random.choices([aluno1, aluno2, aluno3, aluno4], k=4))
