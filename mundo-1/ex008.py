''' Escreva um programa que leia um valor em metros e o exiba convertido em 
centímetros e milímetros. '''

print("##### CONVERSOR DE MEDIDAS #####")
metros = float(input("Digite uma distância em metros: "))
cm = metros * 100
mm = metros * 1000
km = metros * 3.6
hm = metros / 100
dam = metros / 10
dm = metros * 10
print(f'{metros} metros correspondem a:\n'
    f'{km} kilometros\n'
    f'{hm} hectomêtros\n'
    f'{dam} decametros\n'
    f'{dm} decimetros\n'
    f'{cm} centimetros\n'
    f'{mm} miliimetros')
