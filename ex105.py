''' Faça um programa que tenha uma função notas() que pode receber
várias notas de alunos e vai retornar um dicionário'''


def nota(*n, Sit=False):
    '''-->Função nota
    :param n: uma ou mais notas de alunos
    :param Sit: valor opcional, para indicar ou não a situação
    :return: dicionário com varias informaçoes da turma'''
    dic = {}
    cont = len(n)
    dic['Total'] = cont
    max = min = n[0]
    som = 0
    for c in n:
        som += c
        if c > max:
            max = c
        elif c < min:
            min = c
    dic['Maior'] = max
    dic['Menor'] = min
    media = som / cont
    dic['Media'] = media
    if Sit:
        if media >= 8:
            dic['Situação'] = 'Boa'
        elif 6 <= media < 8:
            dic['Situação'] = 'Razoável'
        elif media < 6:
            dic['Situação'] = 'Ruim'
    return dic


# Programa Principal
resp = nota(10, 10, 10, 4.7, Sit=True)
print(resp)
help(nota)
