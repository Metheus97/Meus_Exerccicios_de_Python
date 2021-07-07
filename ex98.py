from time import sleep


def contagem(a, b, c):
    if c < 0:
        c *= -1
    if c == 0:
        c = 1
    print('♦-' * 25)
    print(f'Contagem de {a} até {b} de {c} em {c}')
    if a < b:
        cont = a
        while cont <= b:
            print(f'{cont} ', end='', flush=True)
            cont += c
            sleep(0.5)
        print('FIM!')
    else:
        cont = a
        while cont >= b:
            print(f'{cont} ', end='', flush=True)
            cont -= c
            sleep(0.5)
        print('FIM!')


# Programa principal
contagem(1, 10, 1)
contagem(10, 1, 2)
print('♦-' * 25)
print('Agora é a sua Vez! ')
inic = int(input("Inicio: "))
fim = int(input('Fim:    '))
Pass = int(input('Passos: '))
contagem(inic, fim, Pass)
