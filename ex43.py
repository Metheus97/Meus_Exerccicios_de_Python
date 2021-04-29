from random import randint
itens = ('Pedra', 'Papel', 'Tesoura')
pc = randint(0, 2)
print('''Suas opçoes :
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
jogador = int(input('Qual é sua jogada? '))
print('♦' * 15)
print('Computador jogou {}'.format(itens[pc]))
print('Você jogou {}'.format(itens[jogador]))
print('♦' * 15)
if pc == 0:
    if jogador == 0:
        print('EMPATE!')
    elif jogador == 1:
         print('JOGADOR VENCE!!')
    elif jogador == 2:
        print('COMPUTADOR VENCE!')
    else:
        print('!JOGADA INVÁLIDA!')


elif pc == 1:
    if jogador == 0:
        print('COMPUTADOR VENCE!')
    elif jogador == 1:
        print('EMPATE!')
    elif jogador == 2:
        print('JOGADOR VENCE!!')
    else:
        print('!JOGADA INVÁLIDA!')

elif pc == 2:
    if jogador == 0:
        print('JOGADOR VENCE!!')
    elif jogador == 1:
        print('COMPUTADOR VENCE!')
    elif jogador == 2:
        print('EMPATE!')
    else:
        print('!JOGADA INVÁLIDA!')


