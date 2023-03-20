'''Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o
ano de nascimento de uma pessoa, retornando um valor literal indicando se uma pessoa tem
voto NEGADO, OPCIONAL e OBRIGATÓRIO nas eleições.'''

def voto(ano_nasc):
    '''
    Essa função retorna se é opcional, obrigatorio ou negado o voto pela idade
    ano_nasc: Ano de nascimento
    '''
    from datetime import date
    idade = date.today().year - ano_nasc
    print(f'Com {idade} anos: ', end='')
    if idade < 16:
        return 'VOTO NEGADO'
    if idade >= 16 and idade < 18 or idade >= 70:
        return 'VOTO OPCIONAL'
    if idade >= 18 and idade < 70:
        return 'VOTO OBRIGATORIO'
    

ano_nascimento = int(input('Ano de nascimento: '))
voto_opcao = voto(ano_nascimento)
print(voto_opcao)
