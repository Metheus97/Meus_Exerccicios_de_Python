print('LOJA DO THEUS')
print('-='*30)
tot = totp = menorn = cont = men = 0
while True:
    nome = str(input('Nome do produto:'))
    valor = float(input('Preço: R$  '))
    resp = ' '
    cont += 1
    while resp not in 'SN':
        resp = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    tot += valor
    if valor >= 1000:
        totp += 1
    if cont == 1:
        menorn = nome
        men = valor
    else:
        if valor <= men:
            men = valor
            menorn = nome
    if resp == 'N':
        break
print('-='*30)
print(f'Sua compra custou R$ {tot} \n Temos {totp} com o valor acima de R$ 1000,00 \n O produto mais barato é o {menorn}')

