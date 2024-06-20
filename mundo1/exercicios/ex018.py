import math
an = float(input('Qual ângulo? '))
sen = math.sin(math.radians(an))
print(f'o ângulo de {an} tem o SENO de {sen:.2f}')
cos = math.cos(math.radians(an))
print(f'o ângulo de {an} tem o COSSENO de {cos:.2f}')
tan = math.tan(math.radians(an))
print(f'o ângulo de {an} tem a TANGENTE de {tan:.2f}')
