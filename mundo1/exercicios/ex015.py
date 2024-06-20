a = int(input('Quantos dias alugados? '))
r = float(input('Quantos km rodados? '))
cc = a * 60
kmr = r * 0.15
rf = cc + kmr
print(f'O valor total a pagar é de R${rf:.2f}')

# outra forma com menos variaveis

a = int(input('Quantos dias alugados? '))
r = float(input('Quantos km rodados? '))
vt = (a * 60) + (r * 0.15)
print(f'O valor total a pagar é de R${vt:.2f}')

d = int(input('Quantos dias alugados? '))
km = float(input('Quantos km rodados? '))
t = (d * 60) + (km * 0.15)
print(f'O valor total a pagar é de R${t:.2f}')
