from ex115.lib.interface import *
from ex115.lib.arquivo import *
from time import sleep

arq = 'cadastro.txt'

if not arqExiste(arq):
    criarArquivo(arq)

while True:
    açao = menu(['Cadastrar pessoas', 'Ver lista de pessoas', 'Sair do programa'])
    if açao == 1:
        #cadastrar nova pessoa
        nome = str(input('Nome: '))
        idade = leiaint('Idade: ')
        cadastroPessoa(arq, nome, idade)
    elif açao == 2:
        # listar conteudo
        lerArquivo(arq)
    elif açao == 3:
        cabeçalho('Sair do programa... Até logo!')
        break
    else:
        print('\033[31mERRO! Comando invalido.\033[m')
    sleep(2.5)
