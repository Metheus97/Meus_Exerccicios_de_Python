'''um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento de uma pessoa,
retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL e OBRIGATÓRIO nas eleições'''

from datetime import date
def status():
    global AnoNaci
    anoAtual = date.today().year
    idade = anoAtual - AnoNaci
    if idade < 16:
        print(f'\033[0;31mCom {idade} anos de idade, você não pode votar ainda.')
    if 15 < idade < 18 or idade > 69:
        print(f'\033[0;32mCom {idade} anos de idade, seu voto é opcional.')
    if 17 < idade < 70:
        print(f'\033[0;33mCom {idade} anos de idade, seu voto é obrigatorio.')


# Programa principal
print('Saiba aqui seu status eleitoral!')
print('+=' * 20)

AnoNaci = int(input('Qual o ano do seu nacimento? '))
status()