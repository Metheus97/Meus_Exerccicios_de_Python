from stringcolor import *
print(cs('-*' * 30, '#836FFF'))
peso = float(input('Qual é seu peso? (Kg) '))
altura = float(input('Qual é sua altura? (m) '))
print(cs('-*' * 30, '#836FFF'))
imc = peso / (altura ** 2)
print('O imc desta pessoa é : {:.1f}'.format(imc))
print(cs('-*' * 30, '#836FFF'))
if imc < 18.5:
    print(cs('ABAIXO DO PESO!', '#FF8C00'))
elif imc <= 25:
    print(cs('PESO IDEAL!', '#7CFC00'))
elif imc <= 30:
    print(cs('SOBREPESO!', '#FF8C00'))
elif imc <= 40:
    print(cs('OBESIDADE!', '#FF4500'))
elif imc > 40:
    print(cs('OBESIDADE MORBIDA!', '#DC143C'))
