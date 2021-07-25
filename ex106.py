def ajuda(param):
    from time import sleep
    print(f'\033[0;3;44m~' * 50, f'\n Documentação para a função {param}\n', '~' * 50)
    print('\033[m', flush=True)
    sleep(1.2)
    return help(param)


# Programa principal
while True:
    print(f'\033[0;3;42m~' * 30, '\n  SISTEMA DE AJUDA PYTHON\n', '~' * 30)
    print('\033[m')
    fun = str(input('Função ou Biblioteca > ')).lower()
    if fun == 'fim':
        break
    ajuda(fun)
print(f'\033[0;3;41m~' * 30, '\n  SISTEMA FINALIZADO!\n', '~' * 30)
print('\033[m')
