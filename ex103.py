

def dados(jog='<desconhecido>', gols=0):
    print(f'O jogador {jog} fez o total de {gols} gol(s)')



jogador = str(input('Nome do jogador: '))
g = str(input('Quantos gols ele fez: '))
if g.isnumeric():
    g = int(g)
else:
    g = 0
if jogador.strip() == '':
    dados(gols=g)
else:
    dados(jogador, g)