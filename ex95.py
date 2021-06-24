'''Programa de calculo de aproveitamento de um jogador de futebol no campeonato'''

lista = []

while True:
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
    lista.append(jogador.copy())
    jogador.clear()
    while True:
        res = (str(input('Deseja cadastrar mais jogadores?[S / N] '))).upper()
        if res in 'SN':
            break
        print('ERRO! Por favor, digite apenas S ou N. ')
    if res in 'N':
        break
print('♦-' * 30)
# apresentação
for i in jogador.keys():
    print(f'{i:<15}', end='')
print()
print('♦-' * 30)
for k, j in enumerate(lista):
    print(f'{k:>4} ', end='')
    for d in j.values():
        print(f'{str(d):<15}', end='')
    print()
print('♦-' * 30)
while True:
    busca = int(input('Mostrar dados de qual jogadeor? (999 para parar)'))
    if busca == 999:
        break
    if busca >= len(lista):
        print('ERRO! Não existe este jogador')
    else:
        print(f'---Levantamento do jogador com codigo {busca}! ')
        for i, g in enumerate(lista[busca]['gols']):
            print(f'   No jogo {i+1} fez {g} gols.')
    print('==' * 30)
print('<<   VOLTE SEMPRE!   >>')
