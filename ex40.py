from stringcolor import *

print(cs('-*' * 30, '#836FFF'))
print('FORMAÇAO DE TRINGULOS! ')
print(cs('-*' * 30, '#836FFF'))

r1 = float(input('Primeira reta:'))
r2 = float(input('Segunda reta:'))
r3 = float(input('Terceira reta:'))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print(cs('É totalmente possivel montar um triangulo com este seguimento de retas.', '#00FF00'))
    if r1 == r2 == r3:
        print('Equilatero')
    elif r1 != r2 != r3 != r1:
        print('Escaleno')
    else:
        print('Isosceles')
else:
    print(cs('Com este seguimento de retas não sera possivel fazer um triangulo.','#FF0000'))
