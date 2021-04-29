from stringcolor import *
print(cs('{:=^44}'.format(' SISTEMA DE VENDAS '), '#0000FF'))
preço = float(input('Qual o valor da sua compra:'))
pagamento = int(input('Qual sera a forma de pagamento dessejada\n [1] A vista no dinheiro ou transferencia\n [2] A vista no debito\n [3] Parcelado em ate 2x\n [4] Parcelado em 3x ou mais\n  ?  ='))
if pagamento == 1:
    valor = preço * 0.9
    print('Valor a ser pago R$ {:.2f}'.format(valor))
elif pagamento == 2:
    valor = preço * 0.95
    print('Valor a ser pago será de R$ {:.2f}'.format(valor))
elif pagamento == 3:
    valor = preço / 2
    print('O valor de R$ {:.2f} será pago em 2 parcelas de R$ {:.2f}'.format(preço, valor))
elif pagamento == 4:
    parcela = int(input('Deseja parcelar em quantas vezes? : '))
    valor = preço * 1.2
    valorp = valor / parcela
    print('O valor a ser pago sera de R$ {:.2f} será pago em {} parcelas de R$ {:.2f}'.format(valor, parcela, valorp))
