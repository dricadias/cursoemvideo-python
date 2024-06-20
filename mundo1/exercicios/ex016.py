import math

n = float(input('Digite um número: '))
pt = math.trunc(n)
print(f'O número {n} tem a parte inteira {pt}')

# so com uma funcao importada

from math import trunc

n = float(input('Digite um número: '))
print(f'O número {n} tem a parte inteira {trunc(n)}')

# sem importar modulos

n = float(input('Digite um número: '))
print(f'O número {n} tem a parte inteira {int(n)}')
