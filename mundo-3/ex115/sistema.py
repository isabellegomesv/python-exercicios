''' Crie um pequeno sistema modularizado que permita cadastrar pessoas pelo 
seu nome e idade em um arquivo de texto simples.
O sistema só vai ter 2 opções: cadstrar uma nova pessoa e listar todas as 
pessoas cadastradas. '''

from lib.interface import menu, head, leiaInt

while True:
    r = menu(['Ver pessoas cadastradas', 'Cadastrar nova Pessoa', 'Sair do Sistema'])

    if r == 3:
        head('Saindo do Sistema!')
        break
    if r == 2:
        head('CADASTRE UMA PESSOA')
        nome = input('Nome: ').title().strip()
        idade = leiaInt('Idade: ')

        # Abrindo o arquivo lista.txt e cadastrando a pessoa
        with open('lista.txt', 'a', encoding="utf-8") as arquivo:
            arquivo.write(f'{nome:<25}{f"{idade} anos":<5}\n')         
    elif r == 1:
        head('PESSOAS CADASTRADAS')
        with open('lista.txt', 'r', encoding="utf-8") as arquivo:
            linhas = arquivo.readlines()
            for c in linhas:
                print(c.strip())
    else:
        print('\033[31mERRO! Essa opção não existe, tente novamente.\033[m')
