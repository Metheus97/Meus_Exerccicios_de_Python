from datetime import date
ano = int(input('Coloque seu ano de nascimento:'))
atual = date.today().year
idade = atual - ano
print('Quem nasceu em {} tem {} anos de idade em {}'.format(ano, idade, atual))
if idade == 18:
    print('Deve se alistar este ano')
elif idade > 18:
    saldo = idade - 18
    print('Você deveria ter se alistado a {} anos'.format(saldo))
elif idade < 18:
    saldo = 18 - idade
    print('Você deve se alistar a {} anos'.format(saldo))
