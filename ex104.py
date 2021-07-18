def leiaint(tex):
    while True:
        num = str(input(tex))
        if num.isnumeric():
            num = int(num)
            break
        else:
            print('\033[0;31mERRO DIGITE UM NUMERO VALIDO!\033[m')

    return num

#Programa Principal
n = leiaint('Digite um numero: ')
print(f'O numero que você digitou foi {n}')

