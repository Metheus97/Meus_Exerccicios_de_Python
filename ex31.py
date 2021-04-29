from datetime import date
ano = int(input('Qual ano quer analisar?'))
if ano == 0:
    ano= date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('\033[32mO ano {} é Bissexto!!'.format(ano))
else:
    print('\033[31mO ano {} nao é Bissexto!'.format(ano))
