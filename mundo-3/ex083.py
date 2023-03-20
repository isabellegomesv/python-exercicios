''' Crie um programa onde o usuário digite uma expressão qualquer que use parênteses. 
Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e 
fechados na ordem correta. '''

expressao = input('Digite uma expressão: ')

abre_fecha = []
for c in expressao:
    if c == '(':
        abre_fecha.append(c)
    elif c == ')':
        if len(abre_fecha) > 0:
            abre_fecha.pop()
        else:
            abre_fecha.append(')')
            break

if len(abre_fecha) == 0:
    print('Sua expressão está correta.')
else:
    print('Sua expressão está incorreta.')
