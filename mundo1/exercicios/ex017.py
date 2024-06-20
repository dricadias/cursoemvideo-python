import math
co = float(input('Digite o valor do cateto oposto: '))
ca = float(input('Digite o valor do cateto adjacente: '))
ch = math.pow(co, 2) + math.pow(ca, 2)
hf = math.sqrt(ch)
print(f'O valor da hipotenusa é igual a {hf:.2f}')

# ou como eu sou burro o proprio math tem a funcao de calcular hipotenusa

o = float(input('Digite o valor do cateto oposto: '))
ca = float(input('Digite o valor do cateto adjacente: '))
hi = math.hypot(co, ca)
print(f'O valor da hipotenusa é igual a {hi:.2f}')

# e tem a forma mais complicada ainda mas gracas a deus nao fui tao burro de fazer ela

co = float(input('Digite o valor do cateto oposto: '))
ca = float(input('Digite o valor do cateto adjacente: '))
h = (co ** 2 + ca ** 2) ** (1/2)
print(f'O valor da hipotenusa é igual a {h:.2f}')
