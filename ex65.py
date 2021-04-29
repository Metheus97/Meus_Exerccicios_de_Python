while True:
    num = int(input('Digite um valor para saber sua tabuada: '))
    print('-' * 30)
    if num <= -1:
        break
    for c in range(1, 11):
        res = num * c
        print(f'{num} X {c} = {res}')
    print('-'*30)
print('Programa encerrado, até logo!')

