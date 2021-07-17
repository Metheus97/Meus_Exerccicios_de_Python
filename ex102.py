#(Meu programa q esta certo, mas diferente)
# def fatorial(n, SHOW=True):
#     '''  -> Caulcular o Fatorial de um numero
#     n = o numero que deseja saber o fatorial
#     SHOW(True or False)-- Para mostar a conta ou não'''
#     fat = 1
#     i = 2
#     while i <= n:
#         fat = fat * i
#         i = i + 1
#     if SHOW == True:
#         for c in range(1, n):
#             print(f' {c} X', end='')
#         print(f' {n} = {fat}')
#     else:
#         print(f'{n}! = {fat}')

def fatorial(n, SHOW=True):
    f=1
    for c in range(n, 0, -1):
        if SHOW:
            print(c, end='')
            if c > 1:
                print(' X ', end='')
            else:
                print(' = ', end='')

        f *= c
    return f

#programa principal

print(fatorial(9, SHOW=True))
#help(fatorial)