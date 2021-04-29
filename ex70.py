numeros = ('zero', 'um','dois','três','quatro','cinco','seis',
           'sete','oito','nove','dez','onze','doze','treze','quatorze',
           'quinze','dezesseis','dezessete','dezoito','dezenove','vinte')

while True:
    escolha = int(input(' Escolha um numero de 0 a 20 :'))
    if 0 <= escolha <= 20:
       print('Você escolheu o numero {}'.format(numeros[escolha]))
       cont = str(input('Você deseja continuar?[S/N] ')).upper().strip()
       if cont == 'N':
            break
    else:
        print('Ecolha invalida, Tente novamente.', end='')


