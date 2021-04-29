n = int(input('Digite um numero para ver sua tabuada: '))
for mult in range(1,11,1):
    print('{} X {} = {}'.format(n, mult, n * mult))
