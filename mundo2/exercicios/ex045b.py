from random import randint
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura')
pc = randint(0, 2)
print('''Suas opções:
[0] PEDRA
[1] PAPEL
[2] TESOURA''')
j1 = int(input('Qual é sua jogada? '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')
print('-=' * 12)
print(f'O computador jogou {itens[pc]}')
print(f'Você jogou {itens[j1]}')
print('-=' * 12)
if pc == 0:  # pc jogou PEDRA
    if j1 == 0:
        print('EMPATE')
    elif j1 == 1:
        print('JOGADOR VENCE')
    elif j1 == 2:
        print('COMPUTADOR VENCE')
    else:
        print('JOGADA INVÁLIDA')

elif pc == 1:  # pc jogou PAPEL
    if j1 == 0:
        print('COMPUATDOR VENCE')
    elif j1 == 1:
        print('EMPATE')
    elif j1 == 2:
        print('JOGADOR VENCE')
    else:
        print('JOGADA INVÁLIDA')

elif pc == 2:  # pc jogou TESOURA
    if j1 == 0:
        print('JOGADOR VENCE')
    elif j1 == 1:
        print('COMPUTADOR VENCE')
    elif j1 == 2:
        print('EMPATE')
    else:
        print('JOGADA INVÁLIDA')
