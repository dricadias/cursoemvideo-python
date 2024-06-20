vel = float(input('Digite sua velocidade: '))
v = 7 * (vel - 80)  # o gustavo fez o 'v' ja dentro do if mas acho que isso nao muda muita coisa
if vel > 80:
    print(f'Você foi multado e o valor a pagar é de {v} reais.')
print('Tenha um bom dia! Dirija com segurança!')
