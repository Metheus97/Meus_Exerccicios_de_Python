from random import randint
print('-='*30)
print('VAMOS JOGAR PAR OU IMPAR ?')
print('-='*30)
con = 0
while True:
    while parouimpar not in 'PI:':
        parouimpar = str(input('Par ou impar? [P/I] ')).upper().strip()[0]
    pc = randint(0, 10)
    hum = int(input('Digite um numero: '))
    res = (pc + hum) % 2
    print(f'Você escolheu {hum} e o Computador {pc}.')
    print('-='*30)
    if parouimpar == 'P':
        if res == 0:
            print('Você GANHOU!')
        else:
            break
    elif parouimpar == 'I':
        if res == 1:
            print('Você GANHOU!')
        else:
            break
    con += 1
print(f'Você PERDEU! teve {con} vitorias seguidas')
