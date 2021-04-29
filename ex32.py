a = int(input('Coloque um numero:'))
b = int(input('Coloque outro numero:'))
c = int(input('Coloque um ultimo numero:'))

menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c

maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c

print('Maior numero{}'.format(maior))
print('Menor numero{}'.format(menor))