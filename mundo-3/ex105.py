'''  Faça um programa que tenha uma função notas() que pode receber várias notas de alunos 
e vai retornar um dicionário com as seguintes informações:

-Quantidade de notas
- A maior nota
- A menor nota 
- A média da turma
- A situação (opcional) '''

def notas(*num, sit=False):
    '''
    Retorna um dicionario com informações dos alunos
    :param num: Adiciona um ou mais números.
    :param sit: True ou False para mostrar a situação ou não
    '''
    info_alunos = {
        'total': len(num),
        'maior': max(num),
        'menor': min(num),
        
    }
    media = sum(num) / len(num)
    info_alunos["media"] = f'{media:.1f}'

    if sit:
        if media < 6:
            info_alunos['situação'] = 'RUIM'
        elif media >= 6 and media < 7:
            info_alunos['situação'] = 'RAZOÁVEL'
        elif media >= 7:
            info_alunos['situação'] = 'BOA'
    return info_alunos


print(notas(7, 6, 7, sit=True))
