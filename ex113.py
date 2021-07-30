def leiaint(tex):
    while True:
        try:
            num = int(input(tex))
        except KeyboardInterrupt:
            num = 0
            print('\033[0;31mO USUARIO NÃO DIGITOU!\033[m')
            return num
        except ValueError:
            print('\033[0;31mERRO DIGITE UM NUMERO INTEIRO VALIDO!\033[m')
        else:
            return num


def leiafloat(tex):
    while True:
        try:
            num = float(input(tex))
        except KeyboardInterrupt:
            print('\033[0;31mO USUARIO NÃO DIGITOU!\033[m')
            return 0
        except (ValueError, TypeError):
            print('\033[0;31mERRO DIGITE UM NUMERO REAL VALIDO!\033[m')
            continue
        else:
            return num


# Programa Principal
n = leiaint('Digite um numero inteiro: ')
m = leiafloat('Digite um numero real: ')
print(f'O numero inteiro que você digitou foi {n} e o real {m}')
