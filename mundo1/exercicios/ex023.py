num = input('Digite um número: ')
n = '000' + num
print(f'unidade = {n[-1]}')
print(f'dezena = {n[-2]}')
print(f'centena = {n[-3]}')
print(f'milhar = {n[-4]}')

# modelo do gustavo

num = int(input('Digite um número: '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print(f'Analisando o número {num}')
print(f'Unidade: {u}')
print(f'Dezena: {d}')
print(f'Centena: {c}')
print(f'Milhar: {m}')
