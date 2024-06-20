n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
n3 = int(input('Digite outro número: '))

'''if prim > seg == ter:
    print(f'O maior valor é {prim}')
else:
    if seg > ter and prim:
        print(f'O maior valor é {seg}')
    else:
        print(f'O maior valor é {ter}')

if prim < seg and ter:
    print(f'O menor valor é {prim}')
else:
    if seg < ter or prim:
        print(f'O menor valor é {seg}')
    else:
        print(f'O menor valor é {ter}')'''
# eu burro tentando fazer ☝️☝☝
# pessoa inteligente fazendo 👇👇👇

maior = n1
menor = n1
# Verificando quem é o maior
if n2 > maior:
    maior = n2
if n3 > maior:
    maior = n3
# Verificando quem é o menor
if n2 < menor:
    menor = n2
if n3 < menor:
    menor = n3
print(f'O maior número é o {maior}')
print(f'O menor número é o {menor}')

# e ainda tem essa mais facil ainda (peguei essas 2 dos comentarios)

n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
n3 = int(input('Digite outro número: '))
print(f'O número maior é {max(n1, n2, n3)}. \nO menor é {min(n1, n2, n3)}.')
