''' Crie um programa que leia duas notas de um aluno e calcule sua média,
mostrando uma mensagem no final, de acordo com a média atingida:

- Média abaixo de 5.0: REPROVADO
- Média entre 5.0 e 6.9: RECUPERAÇÃO
- Média 7.0 ou superior: APROVADO '''

print('Calculadora de Média')
nota1 = float(input('Digite sua 1º nota: '))
nota2 = float(input('Digite sua 2º nota: '))
media = (nota1 + nota2) / 2
cores = {
    'amarelo': '\033[33m',
    'vermelho': '\033[31m',
    'verde': '\033[32m',
    'limpa': '\033[m'
}

if media < 5:
    print(f'{cores["vermelho"]}REPROVADO!', end=' ')

elif 7 > media >= 5:
    print(f'{cores["amarelo"]}RECUPERAÇÃO!', end=' ')

else:
    print(f'{cores["verde"]}APROVADO!', end=' ')

print(f'{cores["limpa"]}A sua media foi de {media:.1f}')
