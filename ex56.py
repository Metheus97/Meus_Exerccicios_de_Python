from random import randint
num = randint(0, 10)
print('Tente acertar o numero que escolhi de 0 a 10')
acertou = False
palpites = 0
while not acertou:
    jogador = int(input('Qual é o numero? '))
    palpites += 1
    if jogador == num:
        acertou = True
    else:
        if jogador < num:
            print('Mais ... Tente novamente.')
        elif jogador > num:
            print('Menos... Tente novamente.')
print('Acertou com {} tentativas. Parabens !'.format(palpites))

