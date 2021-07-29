
def dobro(num=0, form=True):
    res = num * 2
    if form:
        res = moeda(res)
    return res


def metade(num=0, form=True):
    res = num / 2
    if form:
        res = moeda(res)
    return res


def aumentar(num=0, porc=0, form=True):
    res = num * ((porc / 100) + 1)
    if form:
        res = moeda(res)
    return res


def diminuir(num=0, porc=0, form=True):
    res = num * (1 - (porc / 100))
    if form:
        res = moeda(res)
    return res


def moeda(valor=0, moedas='R$'):
    return f'{moedas}{valor:.2f}'.replace('.', ',')
