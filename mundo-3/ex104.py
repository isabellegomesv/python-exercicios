''' Crie um programa que tenha a função leiaInt(), que vai funcionar de forma semelhante 
a função input() do Python, só que fazendo a validação para aceitar apenas um valor numérico.
Ex: n = leiaInt('Digite um n: ') '''

def leiaInt(msg):
    while True:
        verifica_numero = input(msg)
        if not verifica_numero.isnumeric(): # Verificando se é um número inteiro.
            print('\033[31mErro! Você não escreveu um número inteiro.\033[m')
        else:
            return verifica_numero

    

# Programa Principal
n = leiaInt('Digite um número: ')
print(f'Você acabou de digitar o número {n}')
