'''Ex de DEF para receber parâmetros e falar qual é o maior'''

import time

def Maior (* N):
    maior = 0
    print('-+' * 20)
    print('Analisando números ...')
    for valor in N:
        print(f'{valor} ', end='', flush=True)
        time.sleep(0.5)
        if valor > maior:
            maior = valor
    cont = len(N)
    print(f' Foram informados {cont} números.')
    print(f'O maior deles é o numero {maior}')

#Programa principal
Maior(2, 10, 4, 6, 9, 8)
Maior(2, 3)
Maior()
