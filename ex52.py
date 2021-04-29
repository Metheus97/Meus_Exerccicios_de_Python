from datetime import date
data = date.today().year
totmaior = 0
totmenor = 0
for c in range(1,8):
    ano = int(input('Em que ano a {}º pessoa nasceu? '.format(c)))
    idade = data - ano
    if idade >= 18:
        totmaior += 1

    else:
        totmenor += 1
print('{} pessoa são menor'.format(totmenor))
print('{} pessoa são maior'.format(totmaior))


