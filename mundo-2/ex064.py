''' Crie um programa que leia vários números inteiros pelo teclado. 
O programa só vai parar quando o usuário digitar o valor 999, que é a 
condição de parada. No final, mostre quantos números foram digitados e 
qual foi a soma entre eles (desconsiderando o flag). '''

n = 0
somar_numeros = []
while n != 999:
    n = int(input('Digite um número: [999 para parar] '))
    if n != 999:
        somar_numeros += [n]

print(f'Você digitou {len(somar_numeros)} números e a soma de todos é igual a {sum(somar_numeros)}')