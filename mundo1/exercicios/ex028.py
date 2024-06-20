import random
from random import randint  # comando pro modo do gustavo
from time import sleep       # comando pro modo do gustavo
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
num = int(input('Em qual número eu pensei? '))
n = [0, 1, 2, 3, 4, 5]
res = random.choice(n)
if num == res:
    print('PARABÉNS! Você acertou!')
else:
    print(f'PARABÉNS!! Você ERROU! haha o número era: {res}')

# modelo do gustavo (prof)

pc = randint(0, 5)  # faz o PC "PENSAR" # mais simples que o random.choice
print('-=-' * 20)
print('Vou pensar em um número entre 0 a 5. Tente adivinhar...')
print('-=-' * 20)
num = int(input('Em qual número eu pensei? '))  # pessoa tenta acertar
print('PROCESSANDO...')
sleep(2)
if num == pc:
    print('PARABÉNS! Você conseguiu me vencer!')
else:
    print(f'Você ERROU! Eu pensei no número {pc} e não no {num}')
