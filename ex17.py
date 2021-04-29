import math

co = float(input('Valor do cateto oposto: '))
ca = float(input('valor do cateto adjacente: '))

hi = math.hypot(co, ca)

print('Sua hipotenusa é = {:.2f}'.format(hi))