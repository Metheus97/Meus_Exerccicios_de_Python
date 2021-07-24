'''um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar(). A primeira função vai
 sortear 5 números e vai colocá-los dentro da lista e a segunda função vai mostrar a soma entre todos os valores pares
 sorteados pela função anterior.'''
from random import randint
from time import sleep

núm = []


def sort(list):
    print('os numeros sorteados são: ', end='')
    for c in range(0, 5):
        num = randint(0, 10)
        list.append(num)
        print(f'{num} ', end='', flush=True)
        sleep(0.5)
    print(' PRONTO!')


def soma(lis):
    res = 0
    for numer in lis:
        if numer % 2 == 0:
            res += numer
    print(f'A soma dos numeros pares é igual a: {res} ')


sort(núm)
soma(núm)
