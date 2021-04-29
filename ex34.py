from stringcolor import *

title = str('AVALIAÇAO PARA FINANCIAMENTO')
print(cs('-=' * 50, '#FFFF00'))
print(cs('{:^100}'.format(title), '#F5F5F5'))
print(cs('-=' * 50, '#FFFF00'))
casa = float(input('Valor da casa:'))
salario = float(input('Valor da sua renda:'))
tempo = int(input('Em quantos anos deseja pagar:'))

mes = tempo * 12
valormensal = casa / mes

if valormensal > salario * 0.3:
    print(cs('Parcela compromete mais de 30% de sua renda. O financiamento foi negado!', '#DC143C'))
else:
    print(cs('O financiamento esta autorizado. A parcela ficara R${:.2f} por mes!'.format(valormensal), '#00FF00'))


