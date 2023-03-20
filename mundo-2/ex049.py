'''  Refaça o DESAFIO 9, mostrando a tabuada de um número que o usuário escolher,
só que agora utilizando um laço for. '''

tab = int(input('Qual tabuada você deseja ver? '))

for c in range(1, 11):
    print(f'{c} x {tab} = {c * tab}')
