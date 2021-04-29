from time import sleep
print('\033[0;30mEscolha dois numeros e o que deseja seber deles!\033[0m')
açao = 0
while açao != 5:
    primeironum: float = float(input('Primeiro numero:'))
    segundonum = float(input('Segundo numero:'))
    print('''Escolha uma das opçoes abaixo:
    [1] SOMAR
    [2] MULTIPLICAR
    [3] MAIOR
    [4] NOVOS NUMEROS
    [5] SAIR DO PROGRAMA''')
    açao = int(input('\033[1;30mDigite o numero correspondente da açao desejada:\033[m '))
    if açao == 1:
        resultado = primeironum + segundonum
        print('{} + {} = {}'.format(primeironum, segundonum, resultado))
    elif açao == 2:
        resultado = primeironum * segundonum
        print('{} * {} = {}'.format(primeironum, segundonum, resultado))
    elif açao == 3:
        if primeironum >= segundonum:
            maior = primeironum
        else:
            maior = segundonum
            print('O maior numero é o {}'.format(maior))
    else:
        print('\033[31mOpção invalida. Tente novamente\033[m')
    print('\033[1;30;44m=-\033[m'*30)
print('Finalizando...')
print(sleep(1),'Programa finalizado.')
