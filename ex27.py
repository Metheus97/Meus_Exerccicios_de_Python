import random
from time import sleep
print('**'*30)
print('!!!MINI GAME!!!')
print('**'*30)
nub = int(input('Digite um numero de 0 a 5, vamos ver se você tem sorte:'))
correta = random.randint(0, 5)
print('PROCESSANDO...')
sleep(2)
print('O numero correto é:', correta)

if nub == correta:
    print('Você é muito sortudo!')
else:
    print('Sabia que ia errar! hehe')
