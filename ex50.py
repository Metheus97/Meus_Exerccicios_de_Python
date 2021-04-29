numero = int(input('Coloque um numero:'))
tot = 0
for c in range(1,numero + 1):
    if numero % c == 0:
        print('\033[32m', end='')
        tot += 1
    else:
        print('\033[31m', end='')
    print('{} '.format(c), end='')
print('\n\033[mO numero {} foi divisivel {} vezes'.format(numero,tot))
if tot == 2:
    print('Por isso ele é primo!')
else:
    print('Por isso ele nao é primo!')

