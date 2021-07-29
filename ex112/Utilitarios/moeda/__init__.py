
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


def resumo(num=0, taxamais=10, taxamenos=5):
    print('-' * 40)
    print('RESUMO DO VALOR'.center(40))
    print('-' * 40)
    print(f'Preço analisado:\t\t\t{moeda(num)}')
    print(f'Dobro do preço: \t\t\t{dobro(num)}')
    print(f'Metade do preço:\t\t\t{metade(num)}')
    print(f'Aumento de {taxamais}% no preço: \t{aumentar(num, taxamais)}')
    print(f'Redução de {taxamenos}% no preço: \t{diminuir(num, taxamenos)}')
    print('-' * 40)


def diminuir(num=0, porc=0, form=True):
    res = num * (1 - (porc / 100))
    if form:
        res = moeda(res)
    return res


def moeda(valor=0, moedas='R$'):
    return f'{moedas}{valor:.2f}'.replace('.', ',')
