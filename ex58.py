'''fac = int(input('Fatorial da numero: '))
n = 1
for num in range(1, fac + 1):
    n *= num
print(n)'''

n = int(input('Digite um valor para calcular seu fatorial: '))
c = n
f = 1
print('Calculando {}! = '.format(n), end='')
while c > 0:
    print('{}'.format(c), end='')
    print('x' if c > 1 else ' = ', end='')
    f *= c
    c -= 1
print('{}'.format(f))
