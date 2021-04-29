from datetime import date
idade = int(input('Coloque aqui o seu ano de nascimento :'))
hoje = date.today().year
anos = hoje - idade
print('Voce tem {} anos de idade'.format(anos))
if anos <= 9:
    print('Competira na categoria mirim')
elif anos <= 14:
    print('Competira na categoria Infantil')
elif anos <= 19:
    print('Competira na categoria junior')
elif anos <= 25:
    print('Competira na categoria senior')
else:
    print('Competira na categoria master')
