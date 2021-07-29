'''Crie um módulo chamado moeda.py que tenha as funções incorporadas aumentar(), diminuir(),
 dobro() e metade(). Faça também um programa que importe esse módulo e use algumas dessas funções.'''


def dobro(num=0):
    res = num * 2
    return res

def metade(num=0):
    res = num / 2
    return res


def aumentar(num=0, porc=0):
    res = num * ((porc / 100) + 1)
    return res


def diminuir(num=0, porc=0):
    res = num * (1 - (porc / 100))
    return res


def moeda(valor=0, moeda='R$'):
    return f'{moeda}{valor:.2f}'.replace('.', ',')
