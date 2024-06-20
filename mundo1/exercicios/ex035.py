r1 = float(input('Digite um comprimento: '))
r2 = float(input('Digite outro comprimento: '))
r3 = float(input('Digite outro comprimento: '))

if r1 + r2 > r3 and r2 + r3 > r1 and r3 + r1 > r2:
    print(f'Esses comprimentos acima PODEM formar um triângulo!')
else:
    print(f'Esses comprimentos acima NÃO PODEM formar um triângulo!')
