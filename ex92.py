# Cadastro de trabalhadores
from datetime import date
trabalhadores = {'nome': str(input('Qual o nome do trabalhador(a): ')), 'nascimento': int(input('Ano de nascimento: ')),
                 'ctps':int(input('Numero da CTPS ( 0 caso não tenha): '))}
data = date.today().year
trabalhadores['idade'] = data - trabalhadores['nascimento']
#Para trabalhadores com CTPS
if trabalhadores['ctps'] != 0:
    trabalhadores['contratação'] = int(input('Ano de contratação: '))
    trabalhadores['salario'] = float(input('Salario de registro:'))
    trabalhadores['aposentadoria'] = trabalhadores['idade'] + (30 - (data - trabalhadores['contratação']))
print('♦-' * 15)
for k, v in trabalhadores.items():
    print(f'- {k} tem o valor {v}')


