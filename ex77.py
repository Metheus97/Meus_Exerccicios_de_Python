lista = []
while True:
    n = int(input('Digite um valor: '))
    if n not in lista:
        lista.append(n)
        print('\033[0;32m Valor adicionado!\033[m')
    else:
        print('\033[0;31m Valor Duplicado não foi aceito.\033[m')

    r = str(input('Quer continuar? [S/N] ')).upper()
    if r in 'N':
        break
print('*=' * 30)
lista.sort()
print(f'Os valores digitados foram {lista}')
