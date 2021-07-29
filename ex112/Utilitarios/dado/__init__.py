def leia_dados(dado):
    while True:
        valor = str(input(dado)).replace(',', '.').strip()
        if valor.isalpha() or valor == '':
            print(f'\033[31mERRO:  \"{valor}\" NÃO É VALIDO\033[m')
        else:
            valor = float(valor)
            return valor
