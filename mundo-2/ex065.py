''' Crie um programa que leia vários números inteiros pelo teclado. No final da execução, 
mostre a média entre todos os valores e qual foi o maior e o menor valores lidos. O programa 
deve perguntar ao usuário se ele quer ou não continuar a digitar valores. '''

contador = maior = menor = soma = 0
resposta = ''
while resposta != 'N':
    n = int(input('Digite um número: '))
    contador += 1
    soma += n
    if contador == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        elif n < menor:
            menor = n

    resposta = input('Você quer continuar? [S/N] ').upper()
    while resposta not in 'SN':
        resposta = input('Ops... Você digitou errado, deseja continuar? [S/N] ').upper()

media = soma / contador
print(f'Você digitou {contador} números e a média foi igual a {media:.2f}')
print('Todos os valores são iguais' if maior == menor else f'O menor valor foi: {menor}\n'
    f'O maior valor foi {maior}')
