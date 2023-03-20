''' Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra “A”,
 em que posição ela aparece a primeira vez e em que posição ela aparece a última vez '''

frase = input('Digite uma frase: ').strip()

print(f'A frase digitada foi: {frase}\n'
    f'A letra "A" aparece {frase.lower().count("a")} vezes na frase.\n'
    f'Aparece pela primeira vez na posição {frase.lower().find("a") + 1}\n'
    f'Pela ultima vez na posição {frase.lower().rfind("a") + 1}')
