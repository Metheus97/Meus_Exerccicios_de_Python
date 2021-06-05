'''Programa de calculo de aproveitamento de um jogador de futebol no campeonato'''

jogador = {'nome': str(input('Qual o nome do jogador? '))}

partidas = int(input('Numero de partidas jogadas: '))
gol = []
tot = 0
for c in range(0, partidas):
    gols = (int(input(f'Quantos gols ele fez na {c + 1}º partida: ')))
    gol.append(gols)
    tot += gols
jogador['gols'] = gol[:]
jogador['total'] = tot

# primeira apresentação
print('♦-' * 30)
print(jogador)
print('♦-' * 30)
# segunda apresentação
for v, k in jogador.items():
    print(f'O campo {v} tem o valor {k}')
print('♦-' * 30)
# Terceira apresentação
print(f'O jogador {jogador["nome"]} jogou {partidas} partidas')
for u in range(0, partidas):
    print(f'    --->Na partida {u + 1} ele fez {gol[u]} gols ')
print(f'Total de gols feitos é de {tot}')

