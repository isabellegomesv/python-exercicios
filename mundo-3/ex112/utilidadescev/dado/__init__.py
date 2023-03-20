def leiaDinheiro(msg):
    while True:
        verifica_numero = input(msg).replace(',', '.').strip()
        if verifica_numero.isalpha():
            print(f'\033[31mErro! "{verifica_numero}" não é um numero.\033[m')
        else:
            return float(verifica_numero)
        