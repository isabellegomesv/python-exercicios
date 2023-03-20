''' Melhore o DESAFIO 61, perguntando para o usuário se ele quer mostrar mais alguns termos. 
O programa encerrará quando ele disser que quer mostrar 0 termos. '''

a1 = int(input('Primeiro termo: '))
r = int(input('Razão: '))
termos = 10
contador = 1
mais = 1
while mais != 0:
    if contador >= termos:
        # Adicionar mais termos na PA
        mais = int(input('Quer calcular mais termos? Digite 0 para sair: '))
        termos += mais
    while contador <= termos:
        print(f'{contador}º = {a1}')
        a1 += r
        contador += 1
print(f'A progressão foi finalizada com {termos} termos mostrados.')
