''' Reescreva a função leiaInt() que fizemos no desafio 104, incluindo agora a possibilidade 
da digitação de um número de tipo inválido. Aproveite e crie também uma função leiaFloat() 
com a mesma funcionalidade. '''

def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[31mERRO! Tente novamente.\033[m')
        except KeyboardInterrupt:
            print('\033[31mO usuario preferiu não digitar esse número\033[m')
            return 0
        else:
            return n


def leiaFloat(msg):
    while True:
        try:
            n = float(input(msg))
        except (ValueError, TypeError):
            print('\033[31mERRO! Tente novamente.\033[m')
        except KeyboardInterrupt:
            print('\033[31mO usuario preferiu não digitar esse número\033[m')
            return 0
        else:
            return n



inteiro = leiaInt('Digite um número Inteiro: ')
real = leiaFloat('Digite um número Real: ')

print(f'O número inteiro digitado foi {inteiro} e o real {real}.')
