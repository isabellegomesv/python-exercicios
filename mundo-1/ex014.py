''' Escreva um programa que converta uma temperatura digitando em graus 
Celsius e converta para graus Fahrenheit '''
print('=-=-' * 10)
print('CONVERSOR DE CELSIUS PARA FAHRENHEIT')
print('=-=-' * 10)

celsius = float(input('Digite uma temperatura em Celsius: '))
f = (celsius * 1.8) + 32

print(f'Convertendo {celsius}°C é igual a {f}°F')
