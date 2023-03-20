def aumentar(n, p, formatado=False):
    '''
    Essa função aumenta a porcentagem de um número
    :param n: Número
    :param p: Porcentagem
    :param formatado: Faz o número voltar formatado
    :return: Retorna o aumento de n
    '''
    aumentado = n + (n * p / 100)
    return aumentado if formatado is False else moeda(aumentado)


def diminuir(n, p, formatado=False):
    '''
    Essa função diminui a porcentagem de um número
    :param n: Número
    :param p: Porcentagem
    :return: Retorna a diminuição de n
    '''
    diminui = n - (n * p / 100)
    return diminui if formatado is False else moeda(diminui)


def dobro(n, formatado=False):
    '''
    Essa função retorna o dobro de n
    :param n: Número
    :return: Retorna o dobro n
    '''
    dobro = n * 2
    return dobro if formatado is False else moeda(dobro)


def metade(n, formatado=False):
    '''
    Essa função retorna a metade de n
    :param n: Número
    :return: Retorna a metade n
    '''
    metade = n / 2
    return metade if formatado is False else moeda(metade)


def moeda(n):
    num = f'{n:.2f}'
    str(num)
    return num.replace('.', ',')

def resumo(n=0, a=10, r=5):
    '''
    Essa função retorna o resumo das funções em moeda.py
    :param n: Número
    :param a: aumento em porcentagem
    :param r: redução em porcetagem
    :return: Retorna o resumo
    '''
    print('-'*30)
    print(f'{"RESUMO DO VALOR":^30}')
    print('-'*30)
    print(f'Preço analisado: \t{moeda(n)}')
    print(f'Dobro do preço: \t{dobro(n, True)}')
    print(f'Metade do preço: \t{metade(n, True)}')
    print(f'{a}% de aumento: \t{aumentar(n, a, True)}')
    print(f'{r}% de redução: \t{diminuir(n, r, True)}')
    print('-'*30)
