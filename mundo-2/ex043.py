''' Desenvolva uma lógica que leia o peso e a altura de uma pessoa,
calcule seu Índice de Massa Corporal (IMC) e mostre seu status, de acordo com a tabela abaixo:

- IMC abaixo de 18,5: Abaixo do Peso
- Entre 18,5 e 25: Peso Ideal
- 25 até 30: Sobrepeso
- 30 até 40: Obesidade
- Acima de 40: Obesidade Mórbida '''
print('==' * 13)
print(' ' * 3, 'CALCULANDO SEU IMC')
print('==' * 13)

peso = float(input('Digite seu peso (Kg): '))
altura = float(input('Digite sua altura (m): '))
imc = peso / (altura * altura)
print(f'O seu IMC é de {imc:.1f},', end=' ')

if imc < 18.5:
    print('você está Abaixo do Peso!')
elif 25 > imc >= 18.5:
    print('você está com o Peso Ideal!')
elif imc <= 30:
    print('você está com Sobrepeso!')
elif imc <= 40:
    print('você esta com Obesidade!')
else:
    print('você está com Obesidade Morbida')
