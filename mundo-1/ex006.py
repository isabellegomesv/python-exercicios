''' Exercício Python 006: Crie um algoritmo que leia um número e mostre o seu dobro, 
triplo e raiz quadrada. '''

n = int(input('Digite um numero: '))
dobro = n * 2
triplo = n * 3
raiz = n ** (1/2)
print(f"O dobro de {n} é igual a {dobro}\n"
    f"O triplo é igual a {triplo}\n"
    f"A raiz quadrada é igual a {raiz:.2f}")
