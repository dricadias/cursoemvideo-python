km = float(input('Digite a distância: '))
d1 = 0.50 * km
d2 = 0.45 * km
if km <= 200:
    print(f'O valor a ser pago é de {d1}')
else:
    print(f'O valor a ser pago é de {d2}')

# modelo simplificado do gustavo (prof)

km = float(input('Qual é a distância da sua viagem? '))
print(f'Você está prestes a começar uma viagem de {km}Km.')  # esse jeito eu ja acho mais baguncadinho
v = km * 0.50 if km <= 200 else km * 0.45              # meio complicado, mas esse ate que ficou legal
print(f'E o valor da sua passagem será de R${v:.2f}')

# ele tambem fez esse aqui que eu achei mais facil que o meu primeiro

km = float(input('Qual é a distância da sua viagem? '))
print(f'Você está prestes a começar uma viagem de {km}Km.')
if km <= 200:
    v = km * 0.50                 # é quase igual, mas achei interessante colocar a
else:                             # variavel apenas na opcao que ela tem que ser usada
    v = km * 0.45
print(f'E o valor da sua passagem será de R${v:.2f}')
